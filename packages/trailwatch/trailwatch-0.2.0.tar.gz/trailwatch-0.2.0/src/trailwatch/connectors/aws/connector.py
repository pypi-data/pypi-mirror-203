import datetime
import logging
import traceback

from types import TracebackType
from typing import TYPE_CHECKING, Type

from requests import Session

from trailwatch.connectors.base import Connector, ConnectorFactory

from .api import TrailwatchApi
from .handler import AwsHandler

if TYPE_CHECKING:
    from trailwatch.config import TrailwatchConfig

logger = logging.getLogger(__name__)


class AwsConnector(Connector):
    def __init__(self, config: "TrailwatchConfig", url: str, api_key: str) -> None:
        self.config = config
        self.api = TrailwatchApi(Session(), url, api_key)
        self.execution_id: str | None = None
        self.handler: AwsHandler | None = None

    def start_execution(self) -> None:
        # Create entries in TrailWatch database
        self.api.upsert_project(
            self.config.project,
            self.config.project_description,
        )
        self.api.upsert_environment(self.config.environment)
        self.api.upsert_job(
            self.config.job,
            self.config.job_description,
            self.config.project,
        )
        self.execution_id = self.api.create_execution(
            self.config.project,
            self.config.environment,
            self.config.job,
            self.config.execution_ttl,
        )

        # Register logging handlers
        if self.execution_id is not None:
            self.handler = AwsHandler(
                self.execution_id,
                self.api,
                self.config.log_ttl,
            )
            for logger_name in self.config.loggers:
                logging.getLogger(logger_name).addHandler(self.handler)

    def finalize_execution(self, status: str, end: datetime.datetime) -> None:
        if self.execution_id is not None:
            self.api.update_execution(self.execution_id, status, end)

        # Remove logging handlers
        if self.handler is not None:
            for logger_name in self.config.loggers:
                logging.getLogger(logger_name).removeHandler(self.handler)

    def handle_exception(
        self,
        timestamp: datetime.datetime,
        exc_type: Type[Exception],
        exc_value: Exception,
        exc_traceback: TracebackType,
    ):
        if self.execution_id is not None:
            self.api.create_error(
                execution_id=self.execution_id,
                timestamp=timestamp,
                name=exc_type.__name__,
                message=str(exc_value),
                traceback="".join(
                    traceback.format_exception(
                        exc_type,
                        value=exc_value,
                        tb=exc_traceback,
                    )
                ),
                ttl=self.config.error_ttl,
            )


class AwsConnectorFactory(ConnectorFactory):
    def __init__(self, url: str, api_key: str) -> None:
        """
        Initialize TrailWatch AWS connector factory.

        Parameters
        ----------
        url : str
            URL pointing to TrailWatch instance deployed on AWS.
            E.g., 'https://somerandomstring.execute-api.us-west-2.amazonaws.com'.
        api_key : str
            API key to be included in the 'x-api-key' header when calling the REST API.

        """
        self.url = url
        self.api_key = api_key

    def __call__(self, config: "TrailwatchConfig") -> AwsConnector:
        return AwsConnector(config, self.url, self.api_key)
