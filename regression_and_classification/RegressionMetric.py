import sklearn.metrics as met
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt

class RegressionMetric:

    def __init__(self, model_name, y_test, prediction):
        self.test_data = y_test
        self.prediction = prediction
        self.model_name = model_name
        self.r2_score = r2_score(y_test, prediction) * 100
        self.MSE = met.mean_squared_error(y_test, prediction)
        self.MAE = met.mean_absolute_error(y_test, prediction)
        self.ME = met.max_error(y_test, prediction)
        # self.MPD = met.mean_poisson_deviance(y_test, prediction)
        self.EVC = met.explained_variance_score(y_test, prediction)

        self.print_result()

        self.plot()

    def plot(self):
        # uncomment to display plots
        plt.title(self.model_name)
        plt.xlabel("Test data")
        plt.ylabel("Predicted data")
        plt.scatter(self.test_data, self.prediction, color="b")
        plt.plot(self.test_data, self.test_data, color="r")
        plt.show()

    def print_result(self):
        print("--------------------", self.model_name, "--------------------")
        print(f'Adjusted R^2: {self.r2_score}')
        print(f'Mean Square Error: {self.MSE}')
        print(f'Mean Absolute Error: {self.MAE}')
        print(f'Max Error: {self.ME}')
        # print(f'Mean Poisson Deviance: {MPD}')
        print(f'Explained variance score: {self.EVC}')
        print("**************************************************")