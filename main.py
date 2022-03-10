from __future__ import print_function, unicode_literals

from cmdQuestions import getMethodAndFunctionType, getStartingPointType, getScalarFunctionCoeff, getStoppingConditions, \
    getNumOfRestartMode, getStartingPointValue, getRangeOfUniformDistribution, getVectorFunctionCoeff, StartingPointType
from gradient_descent import gradientDescent, gradientDescentRandom


def main():
    method, functionType = getMethodAndFunctionType()

    startingPointType = getStartingPointType()

    if method == 'Gradient Descent':
        if functionType == 'F(x)':
            scalarCoeff = getScalarFunctionCoeff()
            conditions = getStoppingConditions()
            numOfRestarts = getNumOfRestartMode()

            if startingPointType == StartingPointType.MANUAL:
                startingPoint = getStartingPointValue()
                gradientDescent(method, scalarCoeff, startingPoint, conditions)

            elif startingPointType == StartingPointType.RANDOM:
                uniformDistributionRange = getRangeOfUniformDistribution()
                gradientDescentRandom(uniformDistributionRange, scalarCoeff, conditions)

        elif functionType == 'G(x)':
            vectorCoeff = getVectorFunctionCoeff()
            # conditions = getStoppingConditions()
            # numOfRestarts = getNumOfRestartMode()
            # if startingPointType == 'Defined Manually':
            #     startingPoint = getStartingPointValue()
            #     gradientDescent(scalarCoeff, startingPoint, conditions)
            # elif startingPointType == 'Randomly generated':
            #     uniformDistributionRange = getRangeOfUniformDistribution()
            #     gradientDescentRandom(uniformDistributionRange, scalarCoeff, conditions)
    elif method == 'Newton':
        if functionType == 'F(x)':
            scalarCoeff = getScalarFunctionCoeff()
            conditions = getStoppingConditions()
            numOfRestarts = getNumOfRestartMode()

            if startingPointType == StartingPointType.MANUAL:

                startingPoint = getStartingPointValue()
                gradientDescent(scalarCoeff, startingPoint, conditions)

            elif startingPointType == StartingPointType.RANDOM:

                uniformDistributionRange = getRangeOfUniformDistribution()
                gradientDescentRandom(uniformDistributionRange, scalarCoeff, conditions)

        elif functionType == 'G(x)':
            vectorCoeff = getVectorFunctionCoeff()
            # conditions = getStoppingConditions()
            # numOfRestarts = getNumOfRestartMode()
            # if startingPointType == 'Defined Manually':
            #     startingPoint = getStartingPointValue()
            #     gradientDescent(scalarCoeff, startingPoint, conditions)
            # elif startingPointType == 'Randomly generated':
            #     uniformDistributionRange = getRangeOfUniformDistribution()
            #     gradientDescentRandom(uniformDistributionRange, scalarCoeff, conditions)


if __name__ == '__main__':
    print("*** Gradient Descent ***")
    main()
