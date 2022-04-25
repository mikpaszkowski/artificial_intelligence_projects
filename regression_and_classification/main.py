import matplotlib.pyplot as plt
import numpy

from decision_tree import decision_tree
from getdata import getdata
from linear_regression import linear_regression
from random_forest import random_forest
from xgboost_regression import xgboost_regression


def display_plots(xgb, dt, rf, lr):
    plt.title("R² models' scores")
    plt.ylabel('R² value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.r2_score, dt.r2_score, rf.r2_score, lr.r2_score]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Mean Square Error")
    plt.ylabel('MSE value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.MSE, dt.MSE, rf.MSE, lr.MSE]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Mean Absolute Error")
    plt.ylabel('MAE value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.MAE, dt.MAE, rf.MAE, lr.MAE]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()

    plt.title("Models' Max Error")
    plt.ylabel('Max Error value')
    models_names = ('XGBoost Reg.', 'Decision Tree', 'Random Forest', 'Linear Reg.')
    y_pos = numpy.arange(len(models_names))
    plt.xticks(y_pos, models_names)
    models_r2s = [xgb.ME, dt.ME, rf.ME, lr.ME]
    plt.bar(y_pos, models_r2s, align='center', alpha=0.5)
    plt.show()


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
