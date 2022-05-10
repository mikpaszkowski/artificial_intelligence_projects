import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler

if __name__ == '__main__':
    dataset = pd.read_csv("Iris.csv")

    # dataset['Species'] = dataset[['Species']].replace(['Iris-setosa','Iris-versicolor','Iris-virginica'],[0,1,2])

    # one_hot = OneHotEncoder()
    # transformed_data = one_hot.fit_transform(dataset['Species'].values.reshape(-1, 1)).toarray()
    #
    # transformed_data = pd.DataFrame(transformed_data,
    #                                 columns=['Iris-setosa', 'Iris-versicolor', 'Iris-virginica'])
    #
    # numeric_columns = [c for c in dataset.columns if dataset[c].dtype != np.dtype('O')]
    # numeric_columns.remove('Id')
    #
    # temp_data = dataset[numeric_columns]
    #
    # # normalazing
    # scaler = MinMaxScaler()
    # temp_data.dropna(axis=1, inplace=True)
    # normalized_data = scaler.fit_transform(temp_data)
    #
    # #standarization
    # standard_scaler = StandardScaler()
    # standardized_data = pd.DataFrame(standard_scaler.fit_transform(temp_data), columns=temp_data.columns, index=temp_data.index)
    #
    ir_features = dataset.drop(columns='Species')
    ir_label = dataset['Species']
    #
    # print(np.array(ir_label))

    X_train, x_test, Y_train, y_test = train_test_split(np.array(ir_features), np.array(ir_label), test_size=0.2, random_state=10)

    mlp_clf = MLPClassifier(hidden_layer_sizes=(150,50),
                            max_iter=3000, activation='relu',
                            solver='sgd')

    # standard_scaler = StandardScaler()
    # scaler = standard_scaler.fit(X_train)
    # trainX_scaled = scaler.transform(X_train)
    # testX_scaled = scaler.transform(x_test)

    mlp_clf.fit(X_train, Y_train)

    print(mlp_clf.score(x_test, y_test))

    y_pred = mlp_clf.predict(x_test)

    print('Accuracy: {:.2f}'.format(accuracy_score(y_test, y_pred)))

    fig = plot_confusion_matrix(mlp_clf, x_test, y_test, display_labels=mlp_clf.classes_)
    fig.figure_.suptitle("Confusion Matrix")
    plot.show()

    print(classification_report(y_test, y_pred))

    plot.plot(mlp_clf.loss_curve_)
    plot.title("Loss Curve", fontsize=14)
    plot.xlabel('Iterations')
    plot.ylabel('Cost')
    plot.show()

    param_grid = {
        'hidden_layer_sizes': [(150, 100, 50), (120, 80, 40), (100, 50, 30)],
        'max_iter': [50, 100, 150],
        'activation': ['tanh', 'relu'],
        'solver': ['sgd', 'adam'],
        'alpha': [0.0001, 0.05],
        'learning_rate': ['constant', 'adaptive'],
    }

    grid = GridSearchCV(mlp_clf, param_grid, n_jobs=-1, cv=5)
    grid.fit(X_train, Y_train)

    print(grid.best_params_)

    grid_predictions = grid.predict(x_test)

    print('Accuracy: {:.2f}'.format(accuracy_score(y_test, grid_predictions)))


