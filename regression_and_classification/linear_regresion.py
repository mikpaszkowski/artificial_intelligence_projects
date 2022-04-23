from statistics import mean
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def mean(x):
    return sum(x)/float(len(x))

def variance(input):
    meanX = mean(input)
    sum = 0
    for x in input:
        sum += (x-meanX)**2
    sum = sum/(len(input)-1)
    return sum
def covarience(x,y):
    meanX = mean(x)
    meanY = mean(y)
    covar = 0.0
    for i in range(len(x)):
        covar += (x[i] - meanX) * (y[i] - meanY)

    covar = covar/(len(x)-1)
    return covar

def simple_linear_regression(train, test):
    predictions = list()
    yintercept, slope = calculateCoefficints(train)
    print("coefficients: ", [yintercept, slope])
    for row in test:
        predictions.append(yintercept+ slope*row[0])
    return predictions

def calculateCoefficints(input):
    x = [row[0] for row in input]
    y = [row[1] for row in input]
    meanX, meanY=  mean(x), mean(y)
    print("x: ", x)
    print("y: ", y)
    slope = covarience(x,y)/variance(x)
    yintercept = meanX - slope * meanY
    return slope, yintercept


def linearRegresion(filename):
    print("variance[1,2,3,4,5,6]: ",variance([1,2,3,4,5,6]))
    print("covarience[5, 12, 18, 23, 45][2, 8, 18, 20, 28]: ",covarience([5, 12, 18, 23, 45],[2, 8, 18, 20, 28]))
    df = pd.read_csv(filename).to_numpy()
    
    x = [row[0] for row in df]
    price = [row[1] for row in df]
    meanSqftLiving = mean(x)
    print("mean sqft_living: ",meanSqftLiving)
    meanPrice = mean(price)
    print("mean price: ", meanPrice)
    print("variance sqft_living: ", variance(x))
    print("variance price: ", variance(price))

    print("covarience of sqft_living and price: ", covarience(x, price))
    # df.plot(kind = 'scatter', x =:][0, y =:][1)
    # plt.show()
    # print("df[sqft_living]:\n",x)
    # print("df[price]:\n",price)
    # print("coefficients: ", calculateCoefficints(df))

    train = list()
    test = list()
    length = len(df)
    for i in range(length):
        if i < length * 0.8: #add row to teach list
            train.append([x[i],price[i]])
        else:
            test.append([x[i],price[i]])
    
    print("function out: ",simple_linear_regression(train, test))



