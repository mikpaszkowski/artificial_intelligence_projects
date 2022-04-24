# from sklearn.linear_model import LinearRegression
from statistics import LinearRegression
import numpy as np
from sklearn import linear_model
from sklearn import metrics as met
import matplotlib.pyplot as plt
from metrics import metrics
from sklearn.model_selection import GridSearchCV


def linear_regresion(X_train, Y_train, X_test, Y_test):
    
    model = linear_model.LinearRegression()
    grid_vals = {'n_jobs': [10, 100, 1000], 'copy_X': [1, 10]}
    grid_lr = GridSearchCV(estimator = model, param_grid = grid_vals, scoring ='r2', cv=6, refit=True, return_train_score=True)

    grid_lr.fit(X_train, Y_train)
    prediction = grid_lr.best_estimator_.predict(X_test)

    metrics("linear regression", Y_test, prediction)