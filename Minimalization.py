import numpy
import random
import time
from cmdQuestions import StoppingConditionType, MethodType, FunctionType


class Minimalization:

    @staticmethod
    def gradientDescent_F(method, coeff, startValue, stopConditions, learnRate=0.001):
        x = startValue
        currNumOfIterations = 0
        startTime = time.time()
        while True:
            currNumOfIterations = currNumOfIterations + 1
            print(x)
            if method == "Gradient Descent":  # gradient descent
                diff = learnRate * (function_F_derivative(coeff, x))
            else:  # newton's formula
                diff = learnRate * (function_F_derivative(coeff, x)) / (
                        6 * coeff.a * x + 2 * coeff.b)  # learnRate*(a*x**3+b*x**2+c*x+d)/(3*a*x**2+2*b*x+c)
            if stopConditions.type == StoppingConditionType.TIMEOUT and time.time() - startTime >= stopConditions.value:
                print("b")
                break
            x = x - diff
            if stopConditions.type == StoppingConditionType.DESIRED_VALUE and x <= stopConditions.value:
                print("c")
                break
            if stopConditions.type == StoppingConditionType.ITERATIONS and currNumOfIterations == stopConditions.value:
                print('d')
                break
        return x, function_F(coeff, x)

    def function_F_derivative(coeff, x):
        return 3 * coeff.a * x ** 2 + 2 * coeff.b * x + coeff.c

    def function_F(coeff, x):
        return coeff.a * x ** 3 + coeff.b * x ** 2 + coeff.c * x + coeff.d

    @staticmethod
    def gradientDescent_G(method, coeff, startValue, stopConditions, learnRate=0.001):
        startTime = time.time()
        x = startValue
        currIteration = 0
        while True:
            if method == MethodType.GRADIENT_DESCENT:  # gradient descent
                diff = learnRate * (gradient_G(coeff, x))
            elif method == MethodType.NEWTON:  # newton's formula
                diff = learnRate * numpy.divide(function_G(coeff, x), derivative_g(coeff, x))
            else:
                raise "TypeError"
            if stopConditions.type == StoppingConditionType.TIMEOUT and time.time() - startTime >= stopConditions.value:
                print("time out")
                break
            x = x - diff
            if stopConditions.type == StoppingConditionType.DESIRED_VALUE and function_G(coeff, x).item(0) <= stopConditions.value:
                print("desired x")
                break
            if stopConditions.type == StoppingConditionType.ITERATIONS and currIteration == stopConditions.value - 1:
                print('d')
                break
            currIteration = currIteration + 1
        return x, d.item(0)

    def gradient_G(coeff, x):
        return numpy.dot(2, numpy.dot(coeff.A, x)) + coeff.b

    def derivative_g(coeff, x):
        return numpy.dot(numpy.transpose(x), numpy.dot(coeff.A, x)) + numpy.dot(numpy.transpose(coeff.b),
                                                                                x) + coeff.c

    @staticmethod
    def gradientDescentRandom(functionType, method, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
        if functionType == FunctionType.SCALAR:
            x = random.randint(uniformDistributionRange.low, uniformDistributionRange.high)
            return Minimalization.gradientDescent_F(method, coeff, x, stopConditions, learnRate)
        else:
            x = numpy.random.normal((uniformDistributionRange.high + uniformDistributionRange.low) / 2,
                                    (uniformDistributionRange.high - uniformDistributionRange.low) / 6)
            return Minimalization.gradientDescent_G(method, coeff, x, stopConditions, learnRate)

    @staticmethod
    def gradientDescentRandomN(n, functionType, method, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
        x_values = [n]
        for i in range(n):
            x_values.append(Minimalization.gradientDescentRandom(functionType, method, uniformDistributionRange, coeff,
                                                                 stopConditions, learnRate))
