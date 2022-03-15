import numpy
import random
import time
from cmdQuestions import StoppingConditionType, MethodType, FunctionType


class Minimalization:

    @staticmethod
    def optimize(functionType, method, coeff, startValue, stopConditions, learnRate=0.001):
        if functionType == FunctionType.SCALAR:
            return Minimalization.optimize_F(method, coeff, startValue, stopConditions, learnRate=0.001)
        else:
            return Minimalization.optimize_G(method, coeff, startValue, stopConditions, learnRate=0.001)

    #refactor optimize_F and optimize_G, the aprt with method type and calculating of diff

    @staticmethod
    def optimize_F(method, coeff, startValue, stopConditions, learnRate=0.001):
        x = startValue
        print("optimize_F called with x = ", x)
        currNumOfIterations = 0
        startTime = time.time()
        while True:
            if method == MethodType.GRADIENT_DESCENT:
                diff = learnRate * Minimalization.function_F_derivative(coeff, x)
            else:
                diff = learnRate * (Minimalization.function_F_derivative(coeff, x)) / (
                        6 * coeff.a * x + 2 * coeff.b)
            if stopConditions.type == StoppingConditionType.TIMEOUT and time.time() - startTime >= stopConditions.value:
                print("Terminated by Timeout stop condition")
                break
            x = x - diff
            if stopConditions.type == StoppingConditionType.DESIRED_VALUE and x <= stopConditions.value:
                print("Terminated by desired value stop condition")
                break
            if stopConditions.type == StoppingConditionType.ITERATIONS and currNumOfIterations == stopConditions.value:
                print('Terminated by number of iterations stop condition')
                break
            currNumOfIterations = currNumOfIterations + 1
        return x, Minimalization.function_F(coeff, x)

    @staticmethod
    def function_F_derivative(coeff, x):
        return 3 * coeff.a * x ** 2 + 2 * coeff.b * x + coeff.c

    @staticmethod
    def function_F(coeff, x):
        return coeff.a * x ** 3 + coeff.b * x ** 2 + coeff.c * x + coeff.d

    @staticmethod
    def optimize_G(method, coeff, startValue, stopConditions, learnRate=0.001):
        startTime = time.time()
        x = startValue
        currIteration = 0
        while True:
            if method == MethodType.GRADIENT_DESCENT:
                diff = learnRate * (Minimalization.derivative_G(coeff, x))
            elif method == MethodType.NEWTON:
                diff = learnRate * numpy.divide(Minimalization.function_G(coeff, x),
                                                Minimalization.derivative_G(coeff, x))
            else:
                raise "TypeError"
            # extract conditions into one method returning message and boolean value
            if stopConditions.type == StoppingConditionType.TIMEOUT and time.time() - startTime >= stopConditions.value:
                print("time out")
                break
            x = x - diff
            if stopConditions.type == StoppingConditionType.DESIRED_VALUE and Minimalization.function_G(coeff, x).item(
                    0) <= stopConditions.value:
                print("desired x")
                break
            if stopConditions.type == StoppingConditionType.ITERATIONS and currIteration == stopConditions.value - 1:
                print('d')
                break
            currIteration = currIteration + 1
        return x, Minimalization.function_G(coeff, x).item(0)

    @staticmethod
    def derivative_G(coeff, x):
        return numpy.dot(2, numpy.dot(coeff.A, x)) + coeff.b

    @staticmethod
    def function_G(coeff, x):
        return numpy.dot(numpy.transpose(x), numpy.dot(coeff.A, x)) + numpy.dot(numpy.transpose(coeff.b),
                                                                                x) + coeff.c

    @staticmethod
    def optimizeRandom(functionType, method, uniformDistributionRange, coeff, stopConditions, learnRate=0.2):
        
        if functionType == FunctionType.SCALAR:
            x = numpy.random.normal((uniformDistributionRange.high + uniformDistributionRange.low) / 2,
                                    (uniformDistributionRange.high - uniformDistributionRange.low) / 6)
            print("calling optimize_F with x = ", x)
            temp = Minimalization.optimize_F(method, coeff, x, stopConditions, learnRate)
            print(temp[0])
            return temp
        else:
            x = numpy.zeros([len(coeff.b), 1])
            for i in range(len(coeff.b)):
                x[i][0] = numpy.random.normal((uniformDistributionRange.high + uniformDistributionRange.low) / 2,
                                    (uniformDistributionRange.high - uniformDistributionRange.low) / 6)

            return Minimalization.optimize_G(method, coeff, x, stopConditions, learnRate)

    @staticmethod
    def optimizeRandomRestartMode(n, functionType, method, uniformDistributionRange, coeff, stopConditions,
                                  learnRate=0.2):
        x = []
        x_values = []
        for i in range(n):
            temp = Minimalization.optimizeRandom(functionType, method, uniformDistributionRange, coeff,
                                                          stopConditions, learnRate)
            x.append(numpy.transpose(temp[0]))
            x_values.append(temp[1])

                                                          
        
       # mean = numpy.mean(x_values)
       # standardDeriviation = numpy.std(x_values)
        print(x)
        return numpy.mean(x), numpy.std(x), numpy.mean(x_values), numpy.std(x_values)
        # return mean value of arguments and function value of that

    @staticmethod
    def optimizeRestartMode(n, functionType, method, coeff, startValue, stopConditions, learnRate=0.2):
        x = []
        x_values = []
        function = Minimalization.optimize_F(method, coeff, startValue, stopConditions, learnRate) \
            if functionType == FunctionType.SCALAR else \
            Minimalization.optimize_G(method, coeff, startValue, stopConditions, learnRate)
        for i in range(n):
            temp = function
            x.append(temp[0])
            x_values.append(temp[1])
        
        return numpy.mean(x), numpy.std(x), numpy.mean(x_values), numpy.std(x_values)
       # mean = numpy.mean(x_values)
       # standardDeriviation = numpy.std(x_values)
       # return mean, standardDeriviation
        #divide optimizeRestartMode into separate logic for F and G

        # return mean value of arguments and function value of that
