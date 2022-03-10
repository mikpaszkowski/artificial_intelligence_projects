import time

import numpy


def gradientDescent(method, coeff, startValue, stopConditions, learnRate=0.001):
    steps = [startValue]
    x = startValue
    startTime = time.time()
    for _ in range(stopConditions.maxNumOfIterations):
        print(x)
        if (method == "Gradient Descent"):  # gradient descent
            diff = learnRate * (3 * coeff.a * x ** 2 + 2 * coeff.b * x + coeff.c)
        elif (type == "Newton"):  # newton's formula
            diff = learnRate * (3 * coeff.a * x ** 2 + 2 * coeff.b * x + coeff.c) / (
                    6 * coeff.a * x + 2 * coeff.b)  # learnRate*(a*x**3+b*x**2+c*x+d)/(3*a*x**2+2*b*x+c)
        if numpy.abs(diff) < stopConditions.tolerance:
            print("a")
            break
        if time.time() - startTime >= stopConditions.timeout:
            print("b")
            break
        x = x - diff
        steps.append(x)
        if x <= stopConditions.desiredValue:
            print("c")
            break
    print(x)
    return x, steps


def optimalisationG(type, coeff, startValue, stopConditions, learnRate=0.001):
    startTime = time.time()
    k = 0
    x = startValue

    for i in range():
        # print(x)
        if type == "g":  # gradient descent
            diff = learnRate * (numpy.dot(2, numpy.dot(coeff.a, x)) + coeff.b)
        elif type == "n":  # newton's formula
            diff = learnRate * numpy.divide(numpy.dot(numpy.transpose(x), numpy.dot(coeff.a, x)) + numpy.dot(numpy.transpose(coeff.b), x) + coeff.c,numpy.dot(2, numpy.dot(coeff.a, x)) + coeff.b)
        else:
            raise "TypeError"
        if numpy.all(numpy.abs(diff) <= stopConditions.tolerance):
            print("tolerance")
            break
        if (time.time() - startTime >= stopConditions.timeOut):
            print("time out")
            break
        x = x - diff
        if (numpy.all(numpy.abs(x) <= stopConditions.desiredX)):
            print("desired x")
            break
    k = k + 1
    print(x)
    print(k)
    return x


def gradientDescentRandom(uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    x = numpy.random.normal((uniformDistributionRange.high + uniformDistributionRange.low) / 2,
                         (uniformDistributionRange.high - uniformDistributionRange.low) / 6)
    gradientDescent(coeff, x, stopConditions, learnRate)


def gradientDescentRandomN(n, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    x_values = [n]
    for i in range(n):
        x_values.append(gradientDescentRandom(uniformDistributionRange, coeff, stopConditions, learnRate))
