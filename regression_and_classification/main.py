
from getdata import getdata
from polynomial_regression import decision_tree
from linear_regresion import linear_regression
from xgboost_regression import xgboost_regression


def main():
    x_train, y_train, x_test, y_test = getdata("kc_house_data_short.csv")

    # logisitc_regression(x_train, y_train, x_test, y_test)
    # xgboost_regression(x_train, y_train, x_test, y_test)
    decision_tree(x_train, y_train, x_test, y_test)
    # random_forest(x_train, y_train, x_test, y_test)
    linear_regression(x_train, y_train, x_test, y_test)
    # analysis("kc_house_data_short.csv")

main()