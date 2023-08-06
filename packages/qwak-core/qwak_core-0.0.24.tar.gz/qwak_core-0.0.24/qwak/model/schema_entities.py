from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from typing import List, Optional, Type

from _qwak_proto.qwak.builds.builds_pb2 import BatchFeature as ProtoBatchFeature
from _qwak_proto.qwak.builds.builds_pb2 import BatchFeatureV1 as ProtoBatchFeatureV1
from _qwak_proto.qwak.builds.builds_pb2 import Entity as ProtoEntity
from _qwak_proto.qwak.builds.builds_pb2 import ExplicitFeature as ProtoExplicitFeature
from _qwak_proto.qwak.builds.builds_pb2 import Feature as ProtoFeature
from _qwak_proto.qwak.builds.builds_pb2 import InferenceOutput as ProtoInferenceOutput
from _qwak_proto.qwak.builds.builds_pb2 import OnTheFlyFeature as ProtoOnTheFlyFeature
from _qwak_proto.qwak.builds.builds_pb2 import Prediction as ProtoPrediction
from _qwak_proto.qwak.builds.builds_pb2 import RequestInput as ProtoRequestInput
from _qwak_proto.qwak.builds.builds_pb2 import SourceFeature as ProtoSourceFeature
from _qwak_proto.qwak.builds.builds_pb2 import (
    StreamingAggregationFeature as ProtoStreamingAggregationFeature,
)
from _qwak_proto.qwak.builds.builds_pb2 import StreamingFeature as ProtoStreamingFeature
from _qwak_proto.qwak.builds.builds_pb2 import (
    StreamingFeatureV1 as ProtoStreamingFeatureV1,
)
from _qwak_proto.qwak.builds.builds_pb2 import ValueType


@dataclass(unsafe_hash=True)
class Entity:
    name: str
    type: Type

    def to_proto(self):
        return ProtoEntity(
            name=self.name, type=ValueType(type=_type_conversion(self.type))
        )


@dataclass
class BaseFeature(ABC):
    name: str

    @abstractmethod
    def to_proto(self):
        pass


@dataclass(unsafe_hash=True)
class ExplicitFeature(BaseFeature):
    type: Type

    def to_proto(self):
        return ProtoFeature(
            explicit_feature=ProtoExplicitFeature(
                name=self.name, type=ValueType(type=_type_conversion(self.type))
            )
        )

    def to_source_proto(self):
        return ProtoSourceFeature(
            explicit_feature=ProtoExplicitFeature(
                name=self.name, type=ValueType(type=_type_conversion(self.type))
            )
        )


@dataclass(unsafe_hash=True)
class RequestInput(BaseFeature):
    type: Type

    def to_proto(self):
        return ProtoFeature(
            request_input=ProtoRequestInput(
                name=self.name, type=ValueType(type=_type_conversion(self.type))
            )
        )

    def to_source_proto(self):
        return ProtoSourceFeature(
            request_input=ProtoRequestInput(
                name=self.name, type=ValueType(type=_type_conversion(self.type))
            )
        )


@dataclass(unsafe_hash=True)
class BatchFeature(BaseFeature):
    entity: Optional[Entity] = None

    def to_proto(self):
        return ProtoFeature(
            batch_feature=ProtoBatchFeature(
                name=self.name, entity=self.entity.to_proto()
            )
        )


@dataclass(unsafe_hash=True)
class BatchFeatureV1(BaseFeature):
    entity: Optional[Entity] = None

    def to_proto(self):
        return ProtoFeature(
            batch_feature_v1=ProtoBatchFeatureV1(
                name=self.name, entity=self.entity.to_proto()
            )
        )


@dataclass(unsafe_hash=True)
class StreamingFeatureV1(BaseFeature):
    entity: Optional[Entity] = None

    def to_proto(self):
        return ProtoFeature(
            batch_feature_v1=ProtoStreamingFeatureV1(
                name=self.name, entity=self.entity.to_proto()
            )
        )


@dataclass(unsafe_hash=True)
class FeatureStoreInput(BaseFeature):
    type: Optional[str] = None
    entity: Optional[Entity] = None

    def to_proto(self):
        pass


@dataclass(unsafe_hash=True)
class StreamingFeature(BaseFeature):
    entity: Entity

    def to_proto(self):
        return ProtoFeature(
            streaming_feature=ProtoStreamingFeature(
                name=self.name, entity=self.entity.to_proto()
            )
        )


@dataclass(unsafe_hash=True)
class StreamingAggregationFeature(BaseFeature):
    entity: Entity

    def to_proto(self):
        return ProtoFeature(
            streaming_aggregation_feature=ProtoStreamingAggregationFeature(
                name=self.name, entity=self.entity.to_proto()
            )
        )


@dataclass
class OnTheFlyFeature(BaseFeature):
    entity: Entity
    source_features: List[ExplicitFeature] = field(default_factory=list)

    def to_proto(self):
        return ProtoFeature(
            on_the_fly_feature=ProtoOnTheFlyFeature(
                name=self.name,
                entity=self.entity.to_proto(),
                source_features=[
                    feature.to_source_proto() for feature in self.source_features
                ],
            )
        )

    def __hash__(self):
        return hash(self.entity) + hash(tuple(self.source_features))


@dataclass(unsafe_hash=True)
class Prediction:
    name: str
    type: type

    def to_proto(self):
        return ProtoPrediction(
            name=self.name, type=ValueType(type=_type_conversion(self.type))
        )


@dataclass(unsafe_hash=True)
class InferenceOutput:
    name: str
    type: type

    def to_proto(self):
        return ProtoInferenceOutput(
            name=self.name, type=ValueType(type=_type_conversion(self.type))
        )


def _type_conversion(type):
    if type == int:
        return ValueType.INT32
    elif type == str:
        return ValueType.STRING
    elif type == bytes:
        return ValueType.BYTES
    elif type == bool:
        return ValueType.BOOL
    elif type == float:
        return ValueType.FLOAT
