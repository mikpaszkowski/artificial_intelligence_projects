from getdata import getdata
from logistic_regresion import logisitc_regression
from support_vector_machine import svm
from random_forest import random_forest


x_train, y_train, x_test, y_test = getdata("kc_house_data_short.csv")
#logisitc_regression(x_train, y_train, x_test, y_test)
svm(x_train, y_train, x_test, y_test)
# random_forest(x_train, y_train, x_test, y_test)