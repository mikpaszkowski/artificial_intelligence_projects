import numpy as np
import time


def gradientDescent(coeff, startValue, stopConditions, learnRate=0.001):
    steps = [startValue]
    x = startValue
    startTime = time.time()
    for _ in range(stopConditions.maxNumOfIterations):
        print(x)
        diff = x - learnRate * (3 * coeff.a * x * x + 2 * coeff.b * x + coeff.c)
        if np.abs(diff) < stopConditions.tolerance:
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


def gradientDescentRandom(uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    x = np.random.normal((uniformDistributionRange.high + uniformDistributionRange.low) / 2, (uniformDistributionRange.high - uniformDistributionRange.low) / 6)
    gradientDescent(coeff, x, stopConditions, learnRate)


def gradientDescentRandomN(n, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
    x_values = [n]
    for i in range(n):
        x_values.append(gradientDescentRandom(uniformDistributionRange, coeff, stopConditions, learnRate))
