import os
from datetime import datetime

from _qwak_proto.qwak.inference.feedback.feedback_pb2 import (
    Actuals,
    ActualValuesRequest,
    ActualValuesResponse,
    ConfigureFeedbackRequest,
    ConfigureFeedbackResponse,
    Entity,
    FeedbackConfig,
)
from _qwak_proto.qwak.inference.feedback.feedback_pb2_grpc import FeedbackServiceStub
from google.protobuf.timestamp_pb2 import Timestamp
from qwak.inner.di_configuration import UserAccountConfiguration
from qwak.inner.tool.grpc.grpc_tools import create_grpc_channel


class FeedbackClient:
    def __init__(
        self,
        model_id=os.environ.get("QWAK_MODEL_ID"),
        models_url_api=None,
        enable_ssl=True,
        enable_auth=True,
    ):
        self.model_id = model_id
        models_url_api = (
            models_url_api
            if models_url_api
            else UserAccountConfiguration().get_models_api()
        )
        channel = create_grpc_channel(
            url=models_url_api, enable_ssl=enable_ssl, enable_auth=enable_auth
        )
        self._feedback_service = FeedbackServiceStub(channel)

    def config(
        self,
        analytics_entity_column: str,
        feedback_entity_column: str,
        model_type: str,
        feedback_config: list,
    ) -> ConfigureFeedbackResponse:
        feedbacks = []
        for config in feedback_config:
            config_map = config.split("=")
            feedbacks.append(
                FeedbackConfig(output_column=config_map[0], actual_tag=config_map[1])
            )

        response = self._feedback_service.ConfigureFeedback(
            ConfigureFeedbackRequest(
                model_id=self.model_id,
                analytics_entity_column=analytics_entity_column,
                feedback_entity_column=feedback_entity_column,
                feedback_config=feedbacks,
                model_type=ConfigureFeedbackRequest.ModelType.Value(model_type.upper()),
            )
        )

        return response

    def actual(
        self,
        entity_name: str,
        entity_value: str,
        tag: str,
        actuals: list,
        timestamp: datetime = None,
    ) -> ActualValuesResponse:
        timestamp = timestamp if timestamp else datetime.now()
        proto_timestamp = Timestamp()
        proto_timestamp.FromDatetime(timestamp)
        feedback_response: ActualValuesResponse = self._feedback_service.PostFeedback(
            ActualValuesRequest(
                model_id=self.model_id,
                entity=Entity(name=entity_name, value=entity_value),
                actuals=Actuals(tag=tag, value=actuals),
                timestamp=proto_timestamp,
            )
        )
        return feedback_response
