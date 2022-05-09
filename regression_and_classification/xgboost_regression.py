import xgboost

from RegressionMetric import RegressionMetric


def xgboost_regression(x_train, y_train, x_test, y_test):
    xgb = xgboost.XGBRegressor(n_estimators=100, learning_rate=0.08, gamma=0, subsample=0.75,
                               colsample_bytree=1, max_depth=7)
    xgb.fit(x_train, y_train)
    predictions = xgb.predict(x_test)
    return RegressionMetric("XGBoost regression", y_test, predictions)
