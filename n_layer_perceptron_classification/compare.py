import timeit

import numpy as np
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier

from write_to_file import write_to_file


def calculate_mse_mae(y_test, pred):
    MSA = 0
    MAE = 0
    for idx, item in enumerate(y_test):
        if item != "Iris-setosa":
            MSA = MSA + pred[idx][0] * pred[idx][0]
            MAE = MAE + pred[idx][0]

        if item != "Iris-versicolor":
            MSA = MSA + pred[idx][1] * pred[idx][1]
            MAE = MAE + pred[idx][1]

        if item != "Iris-virginica":
            MSA = MSA + pred[idx][2] * pred[idx][2]
            MAE = MAE + pred[idx][2]

    return MSA, MAE


def comparison(dataset, hidden_layers):
    ir_features = dataset.drop(columns='Species')
    ir_label = dataset['Species']
    X_train, x_test, Y_train, y_test = train_test_split(np.array(ir_features), np.array(ir_label), test_size=0.2,
                                                        random_state=10)

    accuracy_scores = []
    cross_entropy_loss = []
    max_accuracy = 0
    best = []
    max_accuracy_over_time = 0
    best_over_time = []
    csv_rows = []

    for layers in hidden_layers:
        start = timeit.default_timer()
        mlp_clf = MLPClassifier(hidden_layer_sizes=layers,
                                max_iter=3000, activation='relu',
                                solver='sgd')

        # check_validation_curve(mlp_clf, ir_features, ir_label)
        # check_learning_curve(mlp_clf, ir_features, ir_label)
        # show_confusion_matrix(mlp_clf, ir_features, ir_label)

        mlp_clf.fit(X_train, Y_train)
        time = timeit.default_timer() - start

        y_pred = mlp_clf.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best = layers
        if (accuracy / time) > max_accuracy_over_time:
            max_accuracy_over_time = accuracy
            best_over_time = layers

        print("{0:0.3f}, for: ".format(accuracy), layers)
        accuracy_scores.append(accuracy)
        # calculating cross entropy loss
        pred = mlp_clf.predict_proba(x_test)
        cross_entropy_error = log_loss(y_test, pred)
        cross_entropy_loss.append(cross_entropy_error)

        # checking the balance
        scores = cross_val_score(mlp_clf, X_train, Y_train, cv=3, scoring='accuracy')
        # the samples are balanced across target classes hence the accuracy and the F1-score are almost equal.
        mean_cross_val_accuracy = scores.mean()
        print("Cross Validation Mean Accuracy: %0.2f (+/- %0.2f) \n" % (scores.mean(), scores.std() * 2))

        MSE, MAE = calculate_mse_mae(y_test, pred)

        csv_rows.append([1 if isinstance(layers, int) else len(layers), time, accuracy, mean_cross_val_accuracy, MSE, MAE, cross_entropy_error])

    write_to_file(csv_rows)
    print("best accuracy:", max_accuracy)
    print("best accuracy for: ", best)
    print("best accuracy over time: ", max_accuracy_over_time)
    print("best accuracy over time for: ", best_over_time)
    print(cross_entropy_loss)


def compare(dataset):
    hidden_layers = [
        (10),
        (10, 10),
        (10, 10, 10),
        (10, 10, 10, 10),
        (10, 10, 10, 10, 10),
        (10, 10, 10, 10, 10, 10),
        (10, 10, 10, 10, 10, 10, 10),
        (10, 10, 10, 10, 10, 10, 10, 10),
        (10, 10, 10, 10, 10, 10, 10, 10, 10),
        (10, 10, 10, 10, 10, 10, 10, 10, 10, 10)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (50),
        (50, 50),
        (50, 50, 50),
        (50, 50, 50, 50),
        (50, 50, 50, 50, 50),
        (50, 50, 50, 50, 50, 50),
        (50, 50, 50, 50, 50, 50, 50),
        (50, 50, 50, 50, 50, 50, 50, 50),
        (50, 50, 50, 50, 50, 50, 50, 50, 50),
        (50, 50, 50, 50, 50, 50, 50, 50, 50, 50)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (100),
        (100, 100),
        (100, 100, 100),
        (100, 100, 100, 100),
        (100, 100, 100, 100, 100),
        (100, 100, 100, 100, 100, 100),
        (100, 100, 100, 100, 100, 100, 100),
        (100, 100, 100, 100, 100, 100, 100, 100),
        (100, 100, 100, 100, 100, 100, 100, 100, 100),
        (100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (10),
        (50),
        (10, 10),
        (10, 50),
        (50, 10),
        (50, 50),
        (10, 10, 10),
        (10, 10, 50),
        (10, 50, 10),
        (10, 50, 50),
        (50, 10, 10),
        (50, 10, 50),
        (50, 50, 10),
        (50, 50, 50)
    ]

    comparison(dataset, hidden_layers)
