import numpy as np
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import ShuffleSplit, validation_curve, learning_curve

import matplotlib.pyplot as plot


def check_validation_curve(multilayer_perceptron, data_feature, data_labels):
    # learning curve
    # Calculate accuracy on training and validation set using range of parameter values
    train_scores, valid_scores = validation_curve(multilayer_perceptron, data_feature, data_labels,
                                                  param_name='hidden_layer_sizes', param_range=np.arange(1, 12), cv=3,
                                                  scoring="accuracy")

    # Create range of values for parameter "Number of hidden nodes"
    param_range = np.arange(1, 12)

    # Calculate mean and standard deviation for training set scores
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)

    # Calculate mean and standard deviation for test set scores
    test_scores_mean = np.mean(valid_scores, axis=1)
    test_scores_std = np.std(valid_scores, axis=1)

    # Plot mean accuracy scores for training and test sets
    plot.plot(param_range, train_scores_mean, label="Training score", color="darkorange")
    plot.plot(param_range, test_scores_mean, label="Cross-validation score", color="navy")

    # Plot accurancy bands for training and test sets
    plot.fill_between(param_range, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                      color="gray")
    plot.fill_between(param_range, test_scores_mean - test_scores_std, test_scores_mean + test_scores_std,
                      color="gainsboro")

    # Create plot
    plot.title("Validation Curve MLP")
    plot.xlabel("Number of hidden nodes")
    plot.ylabel("Accuracy")
    plot.tight_layout()
    plot.legend(loc="best")
    plot.show()

    # Columns represent the splits (cv=3) while rows represent the training size
    print('train_scores:\n', train_scores, '\n valid_scores:\n', valid_scores)


def check_learning_curve(multilayer_perceptron, data_feature, data_labels):
    # Cross validation with 100 iterations to get smoother mean test and train
    # score curves, each time with 20% data randomly selected as a validation set.
    cv = ShuffleSplit(n_splits=100, test_size=0.2, random_state=0)
    train_sizes, train_scores, validation_scores = learning_curve(multilayer_perceptron, data_feature, data_labels,
                                                                  cv=cv, n_jobs=5)

    plot.style.use('seaborn')

    # Calculate mean and standard deviation for training set scores
    train_scores_mean = np.mean(train_scores, axis=1)
    train_scores_std = np.std(train_scores, axis=1)

    # Calculate mean and standard deviation for test set scores
    validation_scores_mean = np.mean(validation_scores, axis=1)
    validation_scores_std = np.std(validation_scores, axis=1)

    # Plot the std deviation as a transparent range at each training set size
    plot.fill_between(train_sizes, train_scores_mean - train_scores_std, train_scores_mean + train_scores_std,
                      alpha=0.1, color="lightgreen")
    plot.fill_between(train_sizes, validation_scores_mean - validation_scores_std,
                      validation_scores_mean + validation_scores_std, alpha=0.1, color="b")

    # Plot mean accuracy scores for training and test sets score lines at each training set size

    # Easy to fit a model with a small number of data points (1 to 40)
    plot.plot(train_sizes, train_scores_mean, 'o-', color="lightgreen", label="Training score")
    # Usually,its hard to predict for model with a small number of data points(1 to 40)
    plot.plot(train_sizes, validation_scores_mean, 'o-', color="b", label="Cross-validation score")

    # Create plot
    plot.title("Learning Curve MLP")
    plot.xlabel("Number of training examples")
    plot.ylabel("Score")
    plot.tight_layout()
    plot.legend()
    plot.show()


def show_confusion_matrix(multilayer_perceptron, data_feature, data_labels):
    fig = plot_confusion_matrix(multilayer_perceptron, data_feature, data_labels,
                                display_labels=["Iris-Setosa", "Iris-Versicolor", "Iris-Virginica"])
    fig.figure_.suptitle("Confusion Matrix")
    plot.show()
