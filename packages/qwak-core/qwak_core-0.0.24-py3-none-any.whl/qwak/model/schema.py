from dataclasses import dataclass, field
from typing import Dict, List

from _qwak_proto.qwak.builds.builds_pb2 import ModelSchema as ProtoModelSchema

# Keep unused imports here for backward compatibility
from qwak.model.schema_entities import (
    BaseFeature,
    Entity,
    ExplicitFeature,
    InferenceOutput,
    Prediction,
)


@dataclass
class ModelSchema:
    schema_caching: Dict = field(default_factory=dict)
    is_enrichment: bool = True
    features: List[BaseFeature] = field(default_factory=list)
    entities: List[Entity] = field(default_factory=list)
    predictions: List[Prediction] = field(default_factory=list)
    inference_output: List[InferenceOutput] = field(default_factory=list)

    def __post_init__(self):
        schema_hash = hash(self)
        if schema_hash in self.schema_caching:
            hashed_schema = self.schema_caching[schema_hash]
            self.features = hashed_schema.features
            self.entities = hashed_schema.entities
            self.predictions = hashed_schema.predictions
            self.inference_output = hashed_schema.inference_output
        else:
            self._lower_schema_entities()

    def _lower_schema_entities(self):
        for feature in self.features:
            if not isinstance(feature, ExplicitFeature):
                feature.name = feature.name.lower()
        for entity in self.entities:
            entity.name = entity.name.lower()
        for prediction in self.predictions:
            prediction.name = prediction.name.lower()
        for inference in self.inference_output:
            inference.name = inference.name.lower()

    def to_proto(self):
        return ProtoModelSchema(
            entities=[entity.to_proto() for entity in self.entities],
            features=[feature.to_proto() for feature in self.features],
            predictions=[prediction.to_proto() for prediction in self.predictions],
            inference_output=[
                inference.to_proto() for inference in self.inference_output
            ],
        )

    def __hash__(self):
        return (
            hash(tuple(self.features))
            + hash(tuple(self.entities))
            + hash(tuple(self.predictions))
            + hash(tuple(self.inference_output))
        )
