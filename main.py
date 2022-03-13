from __future__ import print_function, unicode_literals

import numpy
from Minimalization import Minimalization
from cmdQuestions import getMethodAndFunctionType, getStartingPointType, getScalarFunctionCoeff, getStoppingConditions, \
    getNumOfRestartMode, getStartingPointValue, getRangeOfUniformDistribution, getVectorFunctionCoeff, \
    StartingPointType, MethodType, FunctionType


def main():
    method, functionType = getMethodAndFunctionType()

    startingPointType = getStartingPointType()

    scalarCoeff = getScalarFunctionCoeff()
    conditions = getStoppingConditions()
    restartMode = getNumOfRestartMode()

    if startingPointType == StartingPointType.MANUAL:
        startingPoint = getStartingPointValue(functionType)

        if restartMode.isEnabled:
            x, fx = Minimalization.optimizeRestartMode(restartMode.numOfIterations, functionType, method, scalarCoeff, startingPoint,
                                               conditions)
            print(x)
            print(fx)
        else:
            x, fx = Minimalization.optimize(functionType, method, scalarCoeff, startingPoint, conditions)
            print(x)
            print(fx)

    elif startingPointType == StartingPointType.RANDOM:
        uniformDistributionRange = getRangeOfUniformDistribution()
        if restartMode.isEnabled:
            Minimalization.optimizeRandomRestartMode(restartMode.numOfIterations, functionType, method,
                                                     uniformDistributionRange, scalarCoeff, conditions)
        else:
            Minimalization.optimizeRandom(functionType, method, uniformDistributionRange, scalarCoeff, conditions)


if __name__ == '__main__':
    print("*** Gradient Descent ***")
    main()
