# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# Licensed Materials - Property of IBM
# © Copyright IBM Corp. 2021, 2022  All Rights Reserved.
# US Government Users Restricted Rights -Use, duplication or disclosure restricted by
# GSA ADPSchedule Contract with IBM Corp.
# ----------------------------------------------------------------------------------------------------

from typing import List
from marshmallow import Schema, fields, post_dump, post_load, EXCLUDE

from ibm_metrics_plugin.common.utils.constants import ExplainabilityMetricType


class FeatureRange():
    def __init__(self, min: str = None, min_inclusive: bool = None, max: str = None, max_inclusive: bool = None):
        self.min = min
        self.min_inclusive = min_inclusive
        self.max = max
        self.max_inclusive = max_inclusive

class InputFeature:
    def __init__(self, name: str, value: str = None, feature_type: str = None):
        self.name = name
        self.value = value
        self.feature_type = feature_type


class ExplanationFeature():
    def __init__(self, feature_name: str = None, weight: float = None, feature_range: FeatureRange = None, feature_value=None, importance: float = None, positions: List = None, raw_weight=None):
        self.feature_name = feature_name
        self.weight = weight
        self.raw_weight = raw_weight
        self.feature_range = feature_range
        self.feature_value = feature_value
        self.importance = importance
        self.positions = positions


class Prediction():
    def __init__(self, value: str, explanation_features: List[ExplanationFeature] = [], probability=None):
        self.value = value
        self.probability = probability
        self.explanation_features = explanation_features


class LimeExplanation():
    def __init__(self, predictions=None, error=None, input_features = []):
        self.explanation_type = ExplainabilityMetricType.LIME.value
        self.predictions = predictions
        self.error = error
        self.input_features = input_features


class PertinentPositive():
    def __init__(self, features: List[ExplanationFeature] = []):
        self.features = features


class PertinentNegative():
    def __init__(self, features: List[ExplanationFeature] = [], prediction=None, probability=None, is_pn_closest_point_to_pp=None):
        self.features = features
        self.prediction = prediction
        self.probability = probability
        self.is_pn_closest_point_to_pp = is_pn_closest_point_to_pp


class ContrastiveExplanation():
    def __init__(self, pertinent_positive=None, pertinent_negative=None, error=None):
        self.explanation_type = ExplainabilityMetricType.CONTRASTIVE.value
        self.pertinent_positive = pertinent_positive
        self.pertinent_negative = pertinent_negative
        self.error = error


class ErrorTarget:
    def __init__(self, error_type, error_name):
        self.type = error_type
        self.name = error_name


class Error():
    def __init__(self, code, message, vals=[], target=None):
        self.code = code
        self.message = message
        self.vals = vals
        self.target = target


class BaseResponseSchema(Schema):
    class Meta:
        unknown = EXCLUDE

    def value_exist(self, value):
        if type(value) in [bool, int, float]:
            return True
        if value:
            return True
        return False

    @post_dump
    def remove_empty_values(self, data, **kwargs):
        return {key: value for key, value in data.items() if self.value_exist(value)}


class FeatureRangeSchema(BaseResponseSchema):
    min = fields.String()
    min_inclusive = fields.Boolean()
    max = fields.String()
    max_inclusive = fields.Boolean()

    @post_load
    def create_feature_range(self, data):
        return FeatureRange(**data)


class ExplanationFeatureSchema(BaseResponseSchema):
    feature_name = fields.String()
    weight = fields.Number()
    raw_weight = fields.Number()
    feature_range = fields.Nested(FeatureRangeSchema)
    feature_value = fields.String()
    importance = fields.Number()
    positions = fields.List(fields.Raw())

    @post_load
    def create_explanation_feature(self, data):
        return ExplanationFeature(**data)


class PredictionSchema(BaseResponseSchema):
    value = fields.String()
    probability = fields.Number()
    explanation_features = fields.List(fields.Nested(ExplanationFeatureSchema))

    @post_load
    def create_prediction(self, data):
        return Prediction(**data)


class ErrorTargetSchema(BaseResponseSchema):
    type = fields.String()
    name = fields.String()


class ErrorSchema(BaseResponseSchema):
    code = fields.String()
    message = fields.String()
    vals = fields.List(fields.String())
    target = fields.Nested(ErrorTargetSchema)

class InputFeatureSchema(BaseResponseSchema):
    name = fields.String()
    value = fields.String()
    feature_type = fields.String(required=False)

    @post_load
    def create_input_feature(self, data, **kwargs):
        return InputFeature(**data)


class LimeExplanationSchema(BaseResponseSchema):
    explanation_type = fields.String()
    predictions = fields.List(fields.Nested(PredictionSchema))
    error = fields.Nested(ErrorSchema)
    input_features = fields.List(fields.Nested(InputFeatureSchema))


class PertinentPositiveSchema(BaseResponseSchema):
    features = fields.List(fields.Nested(ExplanationFeatureSchema))

    @post_load
    def create_pp(self, data):
        return PertinentPositive(**data)


class PertinentNegativeSchema(BaseResponseSchema):
    features = fields.List(fields.Nested(ExplanationFeatureSchema))
    prediction = fields.String()
    probability = fields.Number()
    is_pn_closest_point_to_pp = fields.Boolean()

    @post_load
    def create_pn(self, data):
        return PertinentNegative(**data)


class ContrastiveExplanationSchema(BaseResponseSchema):
    explanation_type = fields.String()
    pertinent_positive = fields.Nested(PertinentPositiveSchema)
    pertinent_negative = fields.Nested(PertinentNegativeSchema)
    error = fields.Nested(ErrorSchema)


class ImageExplanation:
    def __init__(self, full_image: str, thumbnail_image: str, full_image_url: str, total_features: int, used_features: int):
        self.full_image = full_image
        self.thumbnail_image = thumbnail_image
        self.full_image_url = full_image_url
        self.total_features = total_features
        self.used_features = used_features


class ImageExplanationSchema(BaseResponseSchema):
    full_image = fields.String()
    thumbnail_image = fields.String()
    full_image_url = fields.Url()
    total_features = fields.Integer()
    used_features = fields.Integer()


class ImagePrediction(Prediction):
    def __init__(self, value: str, explanation: List[ImageExplanation]):
        self.value = value
        self.explanation = explanation


class ImagePredictionSchema(PredictionSchema):
    explanation = fields.List(fields.Nested(ImageExplanationSchema))


class LimeImageExplanation():
    def __init__(self,
                 input_features: List[ImageExplanation] = None,
                 predictions: List[ImagePrediction] = None,
                 error=None):
        self.input_features = input_features or []
        self.predictions = predictions or []
        self.explanation_type = ExplainabilityMetricType.LIME.value
        self.error = error

    def set_input_features(self, input_features):
        self.input_features = input_features

    def set_predictions(self, predictions):
        self.predictions = predictions


class LimeImageExplanationSchema(BaseResponseSchema):
    input_features = fields.List(fields.Nested(ImageExplanationSchema))
    predictions = fields.List(fields.Nested(ImagePredictionSchema))
    explanation_type = fields.String()
    error = fields.Nested(ErrorSchema)

    @post_load
    def create_image_response(self, data, **kwargs):
        return LimeImageExplanation(**data)
