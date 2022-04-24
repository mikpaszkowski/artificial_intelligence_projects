from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import GridSearchCV
from metrics import metrics


def logisitc_regression(x_train, y_train, x_test, y_test):
    print("****************** Logsitic Regression ******************")
    log_regr = LogisticRegression()
    log_regr.fit(x_train, y_train)
    pred_log_regr = log_regr.predict(x_test)
    param_grid = { 'penalty': ['l1', 'l2'],'C': [100, 10, 1, 0.1, 1e-2], 'kernel': ['rbf']}
    search_grid = GridSearchCV(LogisticRegression(), param_grid, refit=True, verbose=3)
    search_grid.fit(x_train, y_train)
    print(search_grid.best_params_)
    print(search_grid.best_estimator_)
    search_grid_predictions = search_grid.predict(x_test)
    metrics("logistic_regresion", y_test, search_grid_predictions)