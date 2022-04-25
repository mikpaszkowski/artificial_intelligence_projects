import xgboost
from sklearn.metrics import r2_score

from metrics import metrics


def xgboost_regression(X_train, Y_train, X_test, Y_test):
    xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                               colsample_bytree=1, max_depth=7)
    xgb.fit(X_train, Y_train)
    predictions = xgb.predict(X_test)
    return metrics("XGBoost regression", Y_test, predictions)
