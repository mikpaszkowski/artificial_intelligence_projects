import sklearn.metrics as met
import numpy as np
from sklearn.metrics import r2_score


def metrics(model, y_test, prediction):
    print("--------------------",model,"--------------------")
    print("Acuracy: ", met.accuracy_score(y_test, prediction))
    print("Balanced accuracy: ",met.balanced_accuracy_score(y_test, prediction))
    #print("Average precision: ", met.average_precision_score(y_test, prediction))

    #print("F1 score: ", met.f1_score(y_test, prediction))
    #print("Recall score: ", met.recall_score(y_test, prediction))
    #print("ROC curve:\n", np.asarray(met.roc_curve(y_test, prediction)))
    # print("Area under ROC curve: ", met.roc_auc_score(y_test, prediction, multi_class="ovr"))

    # print("Jaccard score: ", met.jaccard_score(y_test, prediction))

    #print("\nClassification report:\n ", met.classification_report(y_test, prediction))
    print("\nAdjusted R^2:\n ", r2_score(y_test, prediction) * 100)

    print("\nConfusion matrix \n ", np.asarray(met.confusion_matrix(y_test, prediction)))