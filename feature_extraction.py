from steps.base import BaseTransformer
from steps.utils import get_logger

logger = get_logger()


class FeatureDispatcher(BaseTransformer):
    def __init__(self, numerical_columns, categorical_columns, timestamp_columns):
        self.numerical_columns = numerical_columns
        self.categorical_columns = categorical_columns
        self.timestamp_columns = timestamp_columns

    def transform(self, X, y=None, **kwargs):
        outputs = {}
        if self.numerical_columns is not None:
            outputs['numerical_features'] = X[self.numerical_columns].values
            outputs['numerical_feature_names'] = self.numerical_columns

        if self.numerical_columns is not None:
            outputs['categorical_features'] = X[self.categorical_columns].values
            outputs['categorical_feature_names'] = self.categorical_columns

        if self.numerical_columns is not None:
            outputs['timestamp_features'] = X[self.timestamp_columns].values
            outputs['timestamp_feature_names'] = self.timestamp_columns

        return outputs