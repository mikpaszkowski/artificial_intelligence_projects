# from sklearn.linear_model import LinearRegression
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from metrics import metrics


def linear_regression(X_train, Y_train, X_test, Y_test):
    regr = linear_model.LinearRegression()
    regr.fit(X_train, Y_train)
    prediction = regr.predict(X_test).reshape(-1,1)
    plt.scatter(Y_test, prediction, color="b")
    plt.plot(Y_test, Y_test, color="r")
    plt.show()
    print("Y prediction:\n",prediction)
    metrics("linear regression", Y_test, prediction)