import pandas as pd
import numpy as np


def getdata(csvname):
    data = pd.read_csv(csvname).to_numpy()
    print("data: ", data)
    fields = len(data[1])
    length = len(data)
    for x in data:
        x[1] = x[1][:-7]
    train = [[0 for x in range(fields)] for y in range(int(length*0.8)+1)]
    test = [[0 for x in range(fields)] for y in range(int(length*0.2))]

    for i in range(length):
        if i < length * 0.8:
            train[i] = data[i]
        else:
            test[int(i-(length*0.8))][:] = data[i][:]
    print ("train: ", train)
    print ("test: ", test)
    return train, test

