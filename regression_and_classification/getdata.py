import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import seaborn as sns

def preprocessing(df):
    df_cp = df.copy()
    df_cp.drop("id", axis = 1)
    df_cp['date'] = df_cp['date'].str.replace("T000000","")
    df_cp['date'] = pd.to_datetime(df_cp['date'])
    df_cp['year'] = df_cp["date"].dt.year
    df_cp['month'] = df_cp["date"].dt.month
    df_cp["day"] = df_cp["date"].dt.day

    df_cp = df_cp.drop("date", axis = 1)
    # df_cp.info()
    toDelete = np.floor(len(df_cp)*0.02)
    # print("to delete: ", int(toDelete))
    # sns.distplot(df_cp["price"])
    # plt.show()
    df_cp = df_cp.sort_values(["price"], ascending=False).iloc[int(toDelete):]
    # sns.distplot(df_cp["price"])
    # plt.show()
    
    df_cp = df_cp.drop("sqft_above", axis = 1)
    df_cp = df_cp.drop("sqft_living15", axis = 1)


    return df_cp

def getdata(csvname):
    data = pd.read_csv(csvname)
    data = preprocessing(data)

    X = data.drop('price', axis = 1)
    y = data['price']


    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    
    return X_train, Y_train, X_test, Y_test

