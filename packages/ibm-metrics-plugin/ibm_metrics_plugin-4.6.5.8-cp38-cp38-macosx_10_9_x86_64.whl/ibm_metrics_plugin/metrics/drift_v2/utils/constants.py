# ----------------------------------------------------------------------------------------------------
# IBM Confidential
# OCO Source Materials
# 5900-A3Q, 5737-H76
# Copyright IBM Corp. 2022, 2023
# The source code for this program is not published or other-wise divested of its trade
# secrets, irrespective of what has been deposited with the U.S.Copyright Office.
# ----------------------------------------------------------------------------------------------------

from enum import Enum
from functools import total_ordering
from string import Template

RANDOM_SEED = 272
TIMESTAMP_FORMAT = "%Y-%m-%dT%H:%M:%S.%f"
INFINITY = 999999999
PROBABILITY_COLUMN_TEMPLATE = Template("Class Probability for $prediction")
META_MODEL_PROBABILITY_DIFF_COLUMN = "Difference Between Top Two Class Probabilities"
META_MODEL_TARGET_COLUMN = "Target Column for Meta Model"
META_MODEL_CONFIDENCE_COLUMN = "Meta Model Confidence for Incorrect Prediction"
META_MODEL_CLASSIFICATION_COLUMN = "Meta Model Classification"
PREDICTED_ACCURACY_BUFFER_UPPER_BOUND = 0.02
PREDICTED_ACCURACY_BUFFER_LOWER_BOUND = -0.07

DATA_QUALITY_ISSUES_COLUMN = "Data Quality Issues"
MISSING_VALUE = "OpenScale Detected Missing Values"


META_MODEL_SANDBOX_CLASSES = {
    "_reconstruct",
    "ndarray",
    "dtype",
    "scalar",
    "GradientBoostingClassifier",
    "BinomialDeviance",
    "DummyClassifier",
    "DecisionTreeRegressor",
    "__randomstate_ctor",
    "Tree",
    "__RandomState_ctor",

    # HGBT related classes
    "HistGradientBoostingClassifier",
    "BinaryCrossEntropy",
    "_BinMapper",
    "TreePredictor",
}

META_MODEL_SANDBOX_MODULES = {
    "numpy.core.multiarray",
    "numpy",
    "sklearn.ensemble._gb",
    "sklearn.ensemble._gb_losses",
    "sklearn.dummy",
    "sklearn.tree._classes",
    "numpy.random._pickle",
    "sklearn.tree._tree",
    "numpy.random",

    # HGBT related modules
    "sklearn.ensemble._hist_gradient_boosting.gradient_boosting",
    "sklearn.ensemble._hist_gradient_boosting.loss",
    "sklearn.ensemble._hist_gradient_boosting.binning",
    "sklearn.ensemble._hist_gradient_boosting.predictor",
}


class DataSetType(Enum):
    """
    Enum for data set types
    """
    BASELINE = "baseline"
    PRODUCTION = "production"


class ColumnType(Enum):
    """
    Enum for column types
    """
    CATEGORICAL = "categorical"
    NUMERICAL = "numerical"
    PROBABILITY = "probability"
    GENERIC = "generic"


class MetricName(Enum):
    """Enum for metric names"""
    pass


class DiscreteMetricName(MetricName):
    """
    Enum for discrete metric names
    """

    JENSEN_SHANNON = "jensen_shannon"


class ContinuousMetricName(MetricName):
    """
    Enum for continuous metric names
    """

    TOTAL_VARIATION = "total_variation"
    OVERLAP_COEFFICIENT = "overlap_coefficient"


class SignificantIntervalMode(Enum):
    """Enum for significant interval modes"""

    B_GT_P = "baseline_greater_than_production"
    P_GT_B = "production_greater_than_baseline"
    BOTH = "both"


class OperationKind(Enum):
    """Enum for operation kinds"""

    DISCRETE_FEATURE_COUNTS = "discrete_feature_counts"
    CONTINUOUS_FEATURE_COUNTS = "continuous_feature_counts"
    DISCRETE_DISCRETE_FEATURE_COUNTS = "discrete_discrete_feature_counts"
    DISCRETE_CONTINUOUS_FEATURE_COUNTS = "discrete_continuous_feature_counts"
    CONTINUOUS_DISCRETE_FEATURE_COUNTS = "continuous_discrete_feature_counts"
    CONTINUOUS_CONTINUOUS_FEATURE_COUNTS = "continuous_continuous_feature_counts"


class StatisticsKind(Enum):
    """Enum for statistics kinds"""

    DISCRETE = "discrete_statistics"
    CONTINUOUS = "continuous_statistics"


@total_ordering
class ColumnRole(Enum):
    """Enum for column roles"""

    FEATURE = "feature"
    CATEGORICAL = "categorical"
    LABEL = "label"
    PREDICTION = "prediction"
    # PROBABILITY_VECTOR = "probability_vector"
    PROBABILITY_SCORE = "probability_score"
    META_MODEL_TARGET = "meta_model_target"
    META_MODEL_PROBABILITY_SCORE = "meta_model_probability_score"
    META_MODEL_CLASSIFICATION = "meta_model_classification"

    def __lt__(self, other) -> bool:
        priority = [
            "meta_model_target",
            "meta_model_classification",
            "prediction",
            "label",
            "categorical",
            "probability_score",
            "meta_model_probability_score",
            "feature",
            "probability_vector"
        ]

        if self.__class__ is other.__class__:
            # IF 'self' comes after 'other' in the priority array, then it is less important. Return True.
            return priority.index(self.value) > priority.index(other.value)

        raise NotImplementedError

    def __eq__(self, other) -> bool:

        if self.__class__ is other.__class__:
            return self.value == other.value

        raise NotImplementedError


class MetaModelKind(Enum):
    """Enum for Meta Model kinds"""

    SKLEARN_GBT = "scikit_gradient_boosted"
    SKLEARN_HGBT = "scikit_histogram_gradient_boosted"


class DataQualityIssueKind(Enum):
    """Enum for Data Quality Issue Kinds"""

    EMPTY_STRING = "empty_string"
    MISSING_VALUE = "missing_value"
    CATEGORICAL_OUTLIER = "categorical_outlier"
    NUMERICAL_IQR_OUTLIER = "numerical_iqr_outlier"


class PredictionClassification(Enum):
    """Enum for Classifying Meta Model Confidence to Correct/Incorrect/Unsure results."""

    CORRECT = "correct_prediction"
    INCORRECT = "incorrect_prediction"
    UNSURE = "unsure"

class FeatureImportanceInputFormat(Enum):
    """Enum for Feature Importance kinds"""

    # For open-source SHAP library:  np.ndarray
    ND_ARRAY_FORMAT = "ndarray_format"

    # For open-source SHAP library:  list(np.ndarray)
    LIST_ND_ARRAY_FORMAT = "list_ndarray_format"

    # For OpenScale Global Explanation (via metrics plugin or explain service)
    OPENSCALE_GLOBAL_EXPLAIN_FORMAT = "openscale_global_explain_format"

    # Manual Selection of important and most important features
    MANUAL_FORMAT = "manual_format" 

    # JSON format of {feature_name: feature_weight}
    JSON_FORMAT = "json_format"

    # Nested JSON format of {class: {feature_name: feature_weight}}
    NESTED_JSON_FORMAT = "nested_json_format"