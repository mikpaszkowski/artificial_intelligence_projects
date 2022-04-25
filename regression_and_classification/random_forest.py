from sklearn.ensemble import RandomForestRegressor
from metrics import metrics
from sklearn.model_selection import GridSearchCV

def random_forest(X_train, Y_train, X_test, Y_test):

    param_grid = {'min_samples_split' : [3,4,6,10], 'n_estimators' : [70,100], 'random_state': [5] }
    grid_rf = GridSearchCV(RandomForestRegressor(), param_grid, cv = 5, refit=True, verbose = 0, scoring = 'r2')
    grid_rf.fit(X_train, Y_train)

    pred_random_forest = grid_rf.best_estimator_.predict(X_test)

    return metrics("Random forest", Y_test, pred_random_forest)