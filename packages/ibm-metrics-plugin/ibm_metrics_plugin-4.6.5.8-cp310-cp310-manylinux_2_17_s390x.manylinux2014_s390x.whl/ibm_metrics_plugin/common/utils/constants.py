# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# Licensed Materials - Property of IBM
# © Copyright IBM Corp. 2021, 2022  All Rights Reserved.
# US Government Users Restricted Rights -Use, duplication or disclosure restricted by 
# GSA ADPSchedule Contract with IBM Corp.
# ----------------------------------------------------------------------------------------------------

from enum import Enum

CATEGORICAL_DATA_TYPES = [
    "string"
]

NUMERICAL_DATA_TYPES = [
    "integer",
    "float",
    "double",
    "long"
]


class InputDataType(Enum):
    """Supported input data types"""
    STRUCTURED = "structured"
    TEXT = "unstructured_text"
    IMAGE = "unstructured_image"


class ProblemType(Enum):
    """Supported model types"""
    BINARY = "binary"
    MULTICLASS = "multiclass"
    REGRESSION = "regression"

    def is_classification(self):
        return self in (ProblemType.BINARY, ProblemType.MULTICLASS)


class FairnessMetricType(Enum):
    SPD = "statistical_parity_difference"
    SED = "smoothed_empirical_differential_fairness"
    MDSS = "multi_dimensional_subset_scan"
    FST = "WOSFairScoreTransformer"
    MEASURES = "performance_measures"
    MID = "mean_individual_disparity"
    IFPP = "WOSIndividualFairnessPostprocessor"
    TPSD = "WOSTextPrepareStructuredData"
    TP = "WOSTextPerturbations"
    
    @staticmethod
    def values():
        return [e.value for e in FairnessMetricType]

class DriftMetricType(Enum):
    MODEL_OUTPUT_DRIFT = "model_output_drift"
    MODEL_PERFORMANCE_DRIFT = "model_performance_drift"
    INPUT_FEATURE_DRIFT = "input_feature_drift"
    DATA_QUALITY_DRIFT = "data_quality_drift"

    @staticmethod
    def values():
        return [e.value for e in DriftMetricType]

class ExplainabilityMetricType(Enum):
    LIME = "lime"
    CONTRASTIVE = "contrastive"
    SHAP = "shap"
    CONTRASTIVE_ANAMOLY = "contrastive_anamoly"
    PROTODASH = "protodash"
    INPUT_REDUCTION = "input_reduction"
    CONTRASTIVE_TEXT = "contrastive_text"

    @staticmethod
    def values():
        return [e.value for e in ExplainabilityMetricType]


class MetricGroupType(Enum):
    FAIRNESS = "fairness"
    EXPLAINABILITY = "explainability"
    DRIFT = "drift_v2"

    def metrics(self):
        if self.value == MetricGroupType.FAIRNESS.value:
            return FairnessMetricType.values()
        if self.value == MetricGroupType.EXPLAINABILITY.value:
            return ExplainabilityMetricType.values()
        if self.value == MetricGroupType.DRIFT.value:
            return DriftMetricType.values()
