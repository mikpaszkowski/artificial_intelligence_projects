import timeit
import matplotlib.pyplot as plot
import numpy as np
from sklearn.metrics import accuracy_score, log_loss, plot_confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from model_diagnostics import check_validation_curve, check_learning_curve, show_confusion_matrix

cross_entropy_loss = []


def comparison(dataset, hidden_layers):
    ir_features = dataset.drop(columns='Species')
    ir_label = dataset['Species']
    X_train, x_test, Y_train, y_test = train_test_split(np.array(ir_features), np.array(ir_label), test_size=0.2,
                                                        random_state=10)

    accuracy_scores = []
    max_accuracy = 0
    best = []
    max_accuracy_over_time = 0
    best_over_time = []
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
        cross_entropy_loss.append(log_loss(y_test, pred))

        # checking the balance
        scores = cross_val_score(mlp_clf, X_train, Y_train, cv=3, scoring='accuracy')
        # the samples are balanced across target classes hence the accuracy and the F1-score are almost equal.
        f1_scores = cross_val_score(mlp_clf, X_train, Y_train, cv=3, scoring='f1_macro')
        print("Mean Accuracy: %0.2f (+/- %0.2f) \n" % (scores.mean(), scores.std() * 2))

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
