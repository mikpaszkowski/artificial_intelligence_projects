# from sklearn.linear_model import LinearRegression
from sklearn import linear_model
from sklearn.model_selection import GridSearchCV
import matplotlib.pyplot as plt
from metrics import metrics


def linear_regression(X_train, Y_train, X_test, Y_test):
    model = linear_model.LinearRegression()
    grid_vals = {'n_jobs': [10, 100, 1000], 'copy_X': [1, 10]}
    grid_lr = GridSearchCV(estimator=model, param_grid=grid_vals, scoring='r2', cv=6, refit=True,
                           return_train_score=True)

    grid_lr.fit(X_train, Y_train)
    prediction = grid_lr.best_estimator_.predict(X_test)
    return metrics("Linear regression", Y_test, prediction)
