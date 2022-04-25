from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV

from RegressionMetric import RegressionMetric


def random_forest(x_train, y_train, x_test, y_test):
    param_grid = {'min_samples_split': [3, 4, 6, 10], 'n_estimators': [70, 100], 'random_state': [5]}
    grid_rf = GridSearchCV(RandomForestRegressor(), param_grid, cv=5, refit=True, verbose=0, scoring='r2')
    grid_rf.fit(x_train, y_train)

    pred_random_forest = grid_rf.best_estimator_.predict(x_test)

    return RegressionMetric("Random forest", y_test, pred_random_forest)
