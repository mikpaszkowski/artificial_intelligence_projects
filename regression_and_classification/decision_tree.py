from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeRegressor

from RegressionMetric import RegressionMetric


def decision_tree(x_train, y_train, x_test, y_test):
    param_grid = {'max_depth': [7, 8, 9, 10], 'max_features': [11, 12, 13, 14],
                  'max_leaf_nodes': [None, 12, 15, 18, 20], 'min_samples_split': [20, 25, 30], 'random_state': [5]}

    grid_dtree = GridSearchCV(DecisionTreeRegressor(), param_grid, cv=5, refit=True, verbose=0,
                              scoring='neg_mean_squared_error')
    grid_dtree.fit(x_train, y_train)

    pred_dtree = grid_dtree.predict(x_test)
    return RegressionMetric("Decision_tree", y_test, pred_dtree)
