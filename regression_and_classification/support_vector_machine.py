from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from metrics import metrics

def svm(x_train, y_train, x_test, y_test):
    print("****************** Support Vector Machine ******************")
    model = SVC()
    model.fit(x_train, y_train)
    predictions = model.predict(x_test) #leave for a while to compare results with search grid or without
    param_grid = {'C': [1, 10, 100, 1000, 10000], 'gamma': [1e-4, 1e-3, 1e-2, 0.1, 0.2, 0.5, 0.6, 0.9, 1], 'kernel': ['rbf'] }
    search_grid = GridSearchCV(SVC(), param_grid, refit=True, verbose=3)
    search_grid.fit(x_train, y_train)
    print(search_grid.best_params_)
    print(search_grid.best_estimator_)
    search_grid_predictions = search_grid.predict(x_test)
    metrics("SVC", y_test, search_grid_predictions)
