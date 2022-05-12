import timeit

import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, log_loss
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import StandardScaler, LabelEncoder

from model_diagnostics import check_validation_curve, show_confusion_matrix, check_learning_curve
from write_to_file import write_to_file


def calculate_mse_mae(y_test, pred):
    MSA = 0
    MAE = 0
    for idx, item in enumerate(y_test):
        if item[0] != 1:
            MSA = MSA + pred[idx][0] * pred[idx][0]
            MAE = MAE + pred[idx][0]

        if item[1] != 1:
            MSA = MSA + pred[idx][1] * pred[idx][1]
            MAE = MAE + pred[idx][1]

        if item[2] != 1:
            MSA = MSA + pred[idx][2] * pred[idx][2]
            MAE = MAE + pred[idx][2]

    return MSA, MAE


def comparison(dataset, hidden_layers):
    # Label encoding
    le = LabelEncoder()
    le.fit(dataset['Species'])
    dataset['Species'] = le.transform(dataset['Species'])

    # Transfirming Species to a three dimensional vector
    dummies = pd.get_dummies(dataset['Species'], prefix="Species")
    dataset = pd.concat([dataset, dummies], axis=1)
    # print(dataset.head(n=10))

    ir_features = dataset.drop(columns='Species').drop(columns='Species_0').drop(columns='Species_1').drop(
        columns='Species_2')
    ir_label = dataset.drop(columns='Id').drop(columns='SepalLengthCm').drop(columns='SepalWidthCm').drop(
        columns='PetalLengthCm').drop(columns='PetalWidthCm').drop(columns='Species')
    # print(ir_label.head(n=10))

    # ir_label = dataset['Species']
    # ir_features = dataset.drop(columns='Species')

    X_train, x_test, Y_train, y_test = train_test_split(np.array(ir_features), np.array(ir_label), test_size=0.2,
                                                        random_state=10)

    # Mean Normalisation
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
    x_test = sc.transform(x_test)

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

        mlp_clf.fit(X_train, Y_train)

        #to be fixed
        # show_confusion_matrix(mlp_clf, ir_features, dataset['Species'])

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
        print("Cross-entropy error: ", cross_entropy_error)
        # checking the balance
        scores = cross_val_score(mlp_clf, X_train, Y_train, cv=3, scoring='accuracy')
        # the samples are balanced across target classes hence the accuracy and the F1-score are almost equal.
        f1_scores = cross_val_score(mlp_clf, X_train, Y_train, cv=3, scoring='f1_macro')
        print("Mean Accuracy: %0.2f (+/- %0.2f) " % (scores.mean(), scores.std() * 2))
        print("time: ", time)
        mean_cross_val_accuracy = scores.mean()
        print("Cross Validation Mean Accuracy: %0.2f (+/- %0.2f) \n" % (scores.mean(), scores.std() * 2))

        MSE, MAE = calculate_mse_mae(y_test, pred)
        print("MSE: ", MSE)
        print("MAE: ", MAE)
        csv_rows.append(
            [1 if isinstance(layers, int) else len(layers), time, accuracy, mean_cross_val_accuracy, MSE, MAE,
             cross_entropy_error])

    write_to_file(csv_rows)
    print("best accuracy:", max_accuracy)
    print("best accuracy for: ", best)
    print("best accuracy over time: ", max_accuracy_over_time)
    print("best accuracy over time for: ", best_over_time)


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

    # hidden_layers = [
    #     (50),
    #     (50, 50),
    #     (50, 50, 50),
    #     (50, 50, 50, 50),
    #     (50, 50, 50, 50, 50),
    #     (50, 50, 50, 50, 50, 50),
    #     (50, 50, 50, 50, 50, 50, 50),
    #     (50, 50, 50, 50, 50, 50, 50, 50),
    #     (50, 50, 50, 50, 50, 50, 50, 50, 50),
    #     (50, 50, 50, 50, 50, 50, 50, 50, 50, 50)
    # ]
    #
    # comparison(dataset, hidden_layers)
    #
    # hidden_layers = [
    #     (100),
    #     (100, 100),
    #     (100, 100, 100),
    #     (100, 100, 100, 100),
    #     (100, 100, 100, 100, 100),
    #     (100, 100, 100, 100, 100, 100),
    #     (100, 100, 100, 100, 100, 100, 100),
    #     (100, 100, 100, 100, 100, 100, 100, 100),
    #     (100, 100, 100, 100, 100, 100, 100, 100, 100),
    #     (100, 100, 100, 100, 100, 100, 100, 100, 100, 100)
    # ]
    #
    # comparison(dataset, hidden_layers)
    #
    # hidden_layers = [
    #     (10),
    #     (50),
    #     (10, 10),
    #     (10, 50),
    #     (50, 10),
    #     (50, 50),
    #     (10, 10, 10),
    #     (10, 10, 50),
    #     (10, 50, 10),
    #     (10, 50, 50),
    #     (50, 10, 10),
    #     (50, 10, 50),
    #     (50, 50, 10),
    #     (50, 50, 50)
    # ]
    #
    # comparison(dataset, hidden_layers)
