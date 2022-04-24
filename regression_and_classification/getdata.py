import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder

def getdata(csvname):
    data = pd.read_csv(csvname)
    # print("data: ", data)
    # fields = len(data.loc[1])
    # length = len(data)
    # for x in data:
    #     x = x[:-7]
    data['date'] = data['date'].str.replace("T000000","")
    # train = [[0 for x in range(fields)] for y in range(int(length*0.8)+1)]
    # test = [[0 for x in range(fields)] for y in range(int(length*0.2))]

    # for i in range(length):
    #     if i < length * 0.8:
    #         train[i] = data[i]
    #     else:
    #         test[int(i-(length*0.8))][:] = data[i][:]
    # print ("train: ", train)
    # print ("test: ", test)

    # bins = (0, 500000, 99999999999)
    # group_names = ['cheap', 'ekspensive']
    # data['price'] = pd.cut(data['price'], bins = bins, labels = group_names)

    # labels = LabelEncoder()
    # data['price'] = labels.fit_transform(data['price'])
    # data['price'].value_counts()


    # print(data.to_string())
    X = data.drop('price', axis = 1)
    y = data['price']


    X_train, X_test, Y_train, Y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)
    sc = StandardScaler()
    X_train = sc.fit_transform(X_train)
   # Y_train = sc.fit_transform(Y_train).reshape(-1,1)
    print("size X_train: ", np.size(X_train))
    print("size Y_train: ", np.size(Y_train))
    return X_train, Y_train, X_test, Y_test

