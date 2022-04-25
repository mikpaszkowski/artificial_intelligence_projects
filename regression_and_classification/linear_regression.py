from sklearn import linear_model
from sklearn.model_selection import GridSearchCV

from RegressionMetric import RegressionMetric


def linear_regression(x_train, y_train, x_test, y_test):
    model = linear_model.LinearRegression()
    grid_vals = {'n_jobs': [10, 100, 1000], 'copy_X': [1, 10]}
    grid_lr = GridSearchCV(estimator=model, param_grid=grid_vals, scoring='r2', cv=6, refit=True,
                           return_train_score=True)

    grid_lr.fit(x_train, y_train)
    prediction = grid_lr.best_estimator_.predict(x_test)
    return RegressionMetric("Linear regression", y_test, prediction)
