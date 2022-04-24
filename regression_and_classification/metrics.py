import sklearn.metrics as met
import numpy as np
from sklearn.metrics import r2_score


def metrics(model, y_test, prediction):
    print("--------------------",model,"--------------------")
    print("\nAdjusted R^2:\n", r2_score(y_test, prediction) * 100)
    print("\nMean Square Error:\n", met.mean_squared_error(y_test, prediction))
    print("\nMean Absolute Error:\n", met.mean_absolute_error(y_test, prediction))