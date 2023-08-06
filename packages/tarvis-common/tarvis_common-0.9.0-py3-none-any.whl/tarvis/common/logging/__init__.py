from dependency_injector.wiring import Provide, inject
import logging
from logging import Handler
from pendulum.tz import UTC
from tarvis.common import environ, secrets
from tarvis.common.environ import PlatformType, DeploymentType
from tarvis.common.time import datetime

_root_logger = logging.getLogger()
_original_logger_log = None


def _set_log_handler(handler: Handler) -> None:
    global _root_logger
    while _root_logger.hasHandlers():
        _root_logger.removeHandler(_root_logger.handlers[0])
    _root_logger.addHandler(handler)


def _setup_azure_logging() -> None:
    from opencensus.ext.azure.log_exporter import AzureLogHandler

    azure_instrumentation_key = secrets.get_secret("azure_instrumentation_key")
    azure_connection_string = "InstrumentationKey=" + azure_instrumentation_key
    azure_handler = AzureLogHandler(connection_string=azure_connection_string)
    _set_log_handler(azure_handler)


def _setup_gcp_logging() -> None:
    global _original_logger_log
    # noinspection PyProtectedMember
    _original_logger_log = logging.Logger._log

    def _log(
        self,
        level,
        msg,
        args,
        exc_info=None,
        extra=None,
        stack_info=False,
        stacklevel=1,
    ):
        # GCP library will log a text-only message and discard the extra structured
        # logging if the extra is not packaged in their special format
        if extra is not None:
            extra = {"json_fields": extra}
        _original_logger_log(
            self,
            level,
            msg,
            args,
            exc_info=exc_info,
            extra=extra,
            stack_info=stack_info,
            stacklevel=stacklevel,
        )

    logging.Logger._log = _log

    # noinspection PyPackageRequirements
    import google.cloud.logging

    client = google.cloud.logging.Client()
    client.setup_logging()


def _setup_json_logging() -> None:
    global _root_logger
    from pythonjsonlogger import jsonlogger

    class Iso8601JsonFormatter(jsonlogger.JsonFormatter):
        # noinspection SpellCheckingInspection
        def formatTime(self, record, datefmt=None):
            ct = datetime.fromtimestamp(record.created, UTC)
            return ct.to_iso8601_string()

    json_handler = logging.StreamHandler()
    # noinspection SpellCheckingInspection
    json_formatter = Iso8601JsonFormatter(
        fmt="%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    json_handler.setFormatter(json_formatter)
    _set_log_handler(json_handler)


@inject
def load_config(config: dict = Provide["config"]) -> None:
    if environ.deployment in (DeploymentType.DEVELOPMENT, DeploymentType.TESTING):
        logging_config = config.get("logging")
        if logging_config is not None:
            logging_level = logging_config.get("level")
            if logging_level is not None:
                _root_logger.setLevel(logging_level)


match environ.platform:
    case PlatformType.LOCAL | PlatformType.AWS:
        _setup_json_logging()
    case PlatformType.AZURE:
        _setup_azure_logging()
    case PlatformType.GCP | PlatformType.CLIENT:
        _setup_gcp_logging()
    case _:
        raise Exception("Unknown platform")

match environ.deployment:
    case DeploymentType.DEVELOPMENT:
        _root_logger.setLevel(logging.NOTSET)
    case DeploymentType.TESTING:
        _root_logger.setLevel(logging.DEBUG)
    case DeploymentType.STAGING | DeploymentType.PRODUCTION:
        _root_logger.setLevel(logging.INFO)
    case _:
        raise Exception("Unknown deployment")
