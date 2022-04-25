import matplotlib.pyplot as plt
import numpy

from decision_tree import decision_tree
from getdata import getdata
from linear_regression import linear_regression
from random_forest import random_forest
from regression_and_classification.helpers import display_plots
from xgboost_regression import xgboost_regression


def main():
    x_train, y_train, x_test, y_test = getdata("kc_house_data_short.csv")

    metrics_xgb = xgboost_regression(x_train, y_train, x_test, y_test)
    metrics_dt = decision_tree(x_train, y_train, x_test, y_test)
    metrics_rf = random_forest(x_train, y_train, x_test, y_test)
    metrics_lr = linear_regression(x_train, y_train, x_test, y_test)

    #uncomment to display plots
    # display_plots(metrics_xgb, metrics_dt, metrics_rf, metrics_lr)
    # analysis("kc_house_data.csv")

main()
