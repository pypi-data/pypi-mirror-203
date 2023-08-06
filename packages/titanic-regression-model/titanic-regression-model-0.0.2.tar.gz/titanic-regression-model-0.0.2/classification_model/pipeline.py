import xgboost as xgb
from feature_engine.encoding import OneHotEncoder
from feature_engine.imputation import CategoricalImputer, MeanMedianImputer
from feature_engine.selection import DropFeatures
from sklearn.pipeline import Pipeline

from classification_model.config.core import config
from classification_model.processing.cabin_encoder import CabinEncoder

titanic_pipe = Pipeline([

    ('cabin_encoder', CabinEncoder(variables=config.model_config.cabin_vars)),

    # impute numerical variables with the mean
    ('median_imputer', MeanMedianImputer(
        imputation_method='median',
        variables=config.model_config.numerical_vars_with_na)),

    ('missing_imputation', CategoricalImputer(
        imputation_method='missing',
        variables=config.model_config.categorical_vars_with_na_missing)),

    ('frequent_imputation', CategoricalImputer(
        imputation_method='frequent',
        variables=config.model_config.categorical_vars_with_na_frequent)),

    ('drop_features', DropFeatures(
        features_to_drop=config.model_config.drop_features)),

    ('categorical_encoder', OneHotEncoder(
        variables=config.model_config.categorical_vars)),

    ('xgboost', xgb.XGBClassifier(
        **config.model_config.xgb_params.dict(),
        random_state=config.model_config.random_state))

])
