import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
from sklearn.metrics import accuracy_score, plot_confusion_matrix, classification_report, confusion_matrix
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.neural_network import MLPClassifier
from sklearn.preprocessing import OneHotEncoder, MinMaxScaler, StandardScaler, LabelEncoder
from seaborn import set, heatmap


def preprocess(dataset):

    ir_features = dataset.drop(columns='Species')
    ir_label = dataset['Species']
    le = LabelEncoder()
    le.fit(ir_label)
    ir_label_transformed= le.transform(ir_label)
    print("label transformed: ", ir_label_transformed)

    print("ir_label: ", ir_label)
    colors={'Iris-setosa':'red', 'Iris-versicolor':'green','Iris-virginica':'blue'}
    plot.scatter(dataset['SepalLengthCm'], dataset['SepalWidthCm'], c=dataset["Species"].map(colors))
    plot.xlabel("sepalLengthCm")
    plot.ylabel("sepalWidthCm")
    plot.show()

    plot.scatter(dataset['PetalLengthCm'], dataset['PetalWidthCm'], c=dataset["Species"].map(colors))
    plot.xlabel("petalLengthCm")
    plot.ylabel("petalWidthCm")
    plot.show()


    mlp_clf = MLPClassifier(hidden_layer_sizes=(150,50),
                            max_iter=3000, activation='relu',
                            solver='sgd')
    mlp_clf.fit(ir_features, ir_label)
    pred = mlp_clf.predict(ir_features)
    cm=confusion_matrix(ir_label,pred, labels=["Iris-setosa","Iris-versicolor","Iris-virginica"])
    df_cm = pd.DataFrame(cm, range(3), range(3))
    #set(font_scale=1.4)#for label size
    heatmap(df_cm, annot=True, annot_kws={"size": 20})
    plot.xlabel("Predicted Output")
    plot.ylabel("True Output")
    plot.show()