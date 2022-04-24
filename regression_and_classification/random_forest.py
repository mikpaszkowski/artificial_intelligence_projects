from sklearn.ensemble import RandomForestClassifier
from metrics import metrics
def random_forest(X_train, Y_train, X_test, Y_test):
    print("random forest a")
    random_forest = RandomForestClassifier()
    print("random forest b")
    random_forest.fit(X_train, Y_train)
    print("random forest c")
    pred_random_forest = random_forest.predict(X_test)
    print("random forest d")
    metrics("random forest", Y_test, pred_random_forest)