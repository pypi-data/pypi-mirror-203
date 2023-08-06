# scikit-gbm
scikit-learn compatible tools to work with GBM models

## Installation

```
pip install scikit-gbm

# or 

pip install git+https://github.com/krzjoa/scikit-gbm.git

```

## Usage

For the moment, the only available class is `GBMFeaturezier`. It's a wrapper around
scikit-learn GBMs, XGBoost, LightGBM and CatBoost models.

```python


# Classification
from sklearn.datasets import make_classification
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression

from skgbm.preprocessing import GBMFeaturizer
from xgboost import XGBClassifier

X, y = make_classification()
# train_test_split

pipeline = \
    Pipeline([
        ('gbm_featurizer', GBMFeaturizer(XGBClassifier())),
        ('logistic_regression', LogisticRegression())
    ])

# Try also:
# ('gbm_featurizer', GBMFeaturizer(GradientBoostingClassifier())),
# ('gbm_featurizer', GBMFeaturizer(LGBMClassifier())),
# ('gbm_featurizer', GBMFeaturizer(CatBoostClassifier())),


# Regression


```