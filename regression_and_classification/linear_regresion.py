# from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from metrics import metrics


def linear_regresion(X_train, Y_train, X_test, Y_test):
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    prediction = regr.predict(X_test).reshape(-1,1)
    print("Y prediction:\n",prediction)
    # Y_test_float = [float(i) for i in Y_test]
    # Y_test_float.reshape(-1,1)
    Y_test_np = Y_test.to_numpy().reshape(-1,1)
    print("Y_test:\n", Y_test_np)
    # print(regr.score(X_test,Y_test))
    metrics("linear regression", Y_test_np, prediction)