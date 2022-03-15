from conditionCheck import *
from helpers import *
from enums import *


class Minimalization:

    @staticmethod
    def optimize(functionType, method, coeff, startValue, stopConditions, learningRate):
        if functionType == FunctionType.SCALAR:
            return Minimalization.optimize_F(method, coeff, startValue, stopConditions, learningRate)
        else:
            return Minimalization.optimize_G(method, coeff, startValue, stopConditions, learningRate)

    @staticmethod
    def optimize_F(method, coeff, startValue, stopConditions, learnRate=0.001):
        x = startValue
        currNumOfIterations = 0
        startTime = time.time()
        while True:
            diff = learnRate * getGradientValue_F(method, coeff, x)
            isFinished, message = checkConditions_F(stopConditions, coeff, startTime,
                                                                   currNumOfIterations, x)
            if isFinished:
                print(message)
                break
            x = x - diff
            currNumOfIterations = currNumOfIterations + 1
        return x, function_F(coeff, x)

    @staticmethod
    def optimize_G(method, coeff, startValue, stopConditions, learnRate=0.001):
        startTime = time.time()
        x = startValue
        currIteration = 0
        while True:
            diff = learnRate * getGradientValue_G(method, coeff, x)
            isFinished, message = checkConditions_G(stopConditions, coeff, startTime,
                                                                   currIteration, x)
            if isFinished:
                print(message)
                break
            x = x - diff
            currIteration = currIteration + 1
        return x, function_G(coeff, x).item(0)

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
    # divide optimizeRestartMode into separate logic for F and G

    # return mean value of arguments and function value of that