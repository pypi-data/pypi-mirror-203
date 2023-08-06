from sklearn.base import BaseEstimator, TransformerMixin


class CabinEncoder(BaseEstimator, TransformerMixin):
    """Encodes cabin into upper middle and lower on the kaggle titanic dataset"""

    def __init__(self, variables):
        if not isinstance(variables, list):
            raise ValueError('variables should be a list')
        self.variables = variables

        self.cabin_groups = {
                'T': 'Upper',
                'A': 'Upper',
                'B': 'Upper',
                'C': 'Middle',
                'D': 'Middle',
                'E': 'Middle',
                'F': 'Lower',
                'G': 'Lower'
            }

    def fit(self, X, y=None):
        # we need this step to fit the sklearn pipeline
        return self

    def transform(self, X):
        X = X.copy()

        for feature in self.variables:
            cabin_code = X[feature].str.extract(r'([A-Za-z])', expand=False)
            X['Cabin_Level'] = cabin_code.map(self.cabin_groups)

        return X
