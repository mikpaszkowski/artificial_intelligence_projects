import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import timeit
from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler



def comparison(dataset, hidden_layers):
    ir_features = dataset.drop(columns='Species')
    ir_label = dataset['Species']
    X_train, x_test, Y_train, y_test = train_test_split(np.array(ir_features), np.array(ir_label), test_size=0.2, random_state=10)


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

        # standard_scaler = StandardScaler()
        # scaler = standard_scaler.fit(X_train)
        # trainX_scaled = scaler.transform(X_train)
        # testX_scaled = scaler.transform(x_test)

        mlp_clf.fit(X_train, Y_train)
        time = timeit.default_timer() - start
        #print(mlp_clf.score(x_test, y_test))

        y_pred = mlp_clf.predict(x_test)
        accuracy = accuracy_score(y_test, y_pred)
        if accuracy > max_accuracy:
            max_accuracy = accuracy
            best = layers
        if (accuracy/time) > max_accuracy_over_time:
            max_accuracy_over_time = accuracy
            best_over_time = layers
        print("{0:0.3f}, for: ".format(accuracy), layers)
        accuracy_scores.append(accuracy)
    print("best accuracy:", max_accuracy)
    print("best accuracy for: ", best)
    print("best accuracy over time: ", max_accuracy_over_time)
    print("best accuracy over time for: ", best_over_time)

def compare(dataset):

    hidden_layers = [
        (10),
        (10,10),
        (10,10,10),
        (10,10,10,10),
        (10,10,10,10,10),
        (10,10,10,10,10,10),
        (10,10,10,10,10,10,10),
        (10,10,10,10,10,10,10,10),
        (10,10,10,10,10,10,10,10,10),
        (10,10,10,10,10,10,10,10,10,10)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (50),
        (50,50),
        (50,50,50),
        (50,50,50,50),
        (50,50,50,50,50),
        (50,50,50,50,50,50),
        (50,50,50,50,50,50,50),
        (50,50,50,50,50,50,50,50),
        (50,50,50,50,50,50,50,50,50),
        (50,50,50,50,50,50,50,50,50,50)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (100),
        (100,100),
        (100,100,100),
        (100,100,100,100),
        (100,100,100,100,100),
        (100,100,100,100,100,100),
        (100,100,100,100,100,100,100),
        (100,100,100,100,100,100,100,100),
        (100,100,100,100,100,100,100,100,100),
        (100,100,100,100,100,100,100,100,100,100)
    ]

    comparison(dataset, hidden_layers)

    hidden_layers = [
        (10),
        (50),
        (10,10),
        (10,50),
        (50,10),
        (50,50),
        (10,10,10),
        (10,10,50),
        (10,50,10),
        (10,50,50),
        (50,10,10),
        (50,10,50),
        (50,50,10),
        (50,50,50)
    ]

    comparison(dataset, hidden_layers)
