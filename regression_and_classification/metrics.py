import sklearn.metrics as met
import numpy as np
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

from RegressionMetric import RegressionMetric


def metrics(model, Y_test, prediction):
    r2_score_val = r2_score(Y_test, prediction) * 100
    MSE = met.mean_squared_error(Y_test, prediction)
    MAE = met.mean_absolute_error(Y_test, prediction)
    ME = met.max_error(Y_test, prediction)
    # MPD = met.mean_poisson_deviance(Y_test, prediction)
    EVC = met.explained_variance_score(Y_test, prediction)
    print("--------------------",model,"--------------------")
    print(f'Adjusted R^2: {r2_score_val}')
    print(f'Mean Square Error: {MSE}')
    print(f'Mean Absolute Error: {MAE}')
    print(f'Max Error: {ME}')
    # print(f'Mean Poisson Deviance: {MPD}')
    print(f'Explained variance score: {EVC}')
    print("**************************************************")

    #uncomment to display plots
    # plt.title(model)
    # plt.xlabel("Test data")
    # plt.ylabel("Predicted data")
    # plt.scatter(Y_test, prediction, color="b")
    # plt.plot(Y_test, Y_test, color="r")
    # plt.show()

    return RegressionMetric(r2_score_val, MSE, MAE, ME, 0, EVC)