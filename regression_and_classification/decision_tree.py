from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from metrics import metrics


def decision_tree(X_train, Y_train, X_test, Y_test):
    param_grid = {'max_depth': [7, 8, 9, 10], 'max_features': [11, 12, 13, 14],
                  'max_leaf_nodes': [None, 12, 15, 18, 20], 'min_samples_split': [20, 25, 30], 'random_state': [5]}

    decision_tree = DecisionTreeRegressor()
    grid_dtree = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5, refit=True, verbose=0,
                              scoring='neg_mean_squared_error')
    grid_dtree.fit(X_train, Y_train)

    pred_dtree = grid_dtree.predict(X_test)
    metrics("decision_tree", Y_test, pred_dtree)
