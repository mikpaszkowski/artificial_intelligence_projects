from __future__ import print_function, unicode_literals

import numpy
from Minimalization import Minimalization
from cmdQuestions import getMethodAndFunctionType, getStartingPointType, getScalarFunctionCoeff, getStoppingConditions, \
    getNumOfRestartMode, getStartingPointValue, getRangeOfUniformDistribution, getVectorFunctionCoeff, \
    StartingPointType, MethodType, FunctionType


def main():
    method, functionType = getMethodAndFunctionType()

    startingPointType = getStartingPointType()
    if functionType == functionType.SCALAR:
        print("function type f(x)")
        print(functionType)
        coeff = getScalarFunctionCoeff()
    else:
        print("function type g(x)")
        print(functionType)
        coeff = getVectorFunctionCoeff()
    conditions = getStoppingConditions()
    restartMode = getNumOfRestartMode()

    if startingPointType == StartingPointType.MANUAL:
        startingPoint = getStartingPointValue(functionType)

        if restartMode.isEnabled:
            mean_x, standard_der_x, mean_value, standard_der_value = Minimalization.optimizeRestartMode(restartMode.numOfIterations, functionType, method, coeff, startingPoint,
                                               conditions)
            print("mean x: ",mean_x)
            print("standard deriviation from mean x: ",standard_der_x)
            print("mean function value: ",mean_value)
            print("standard deriviation from mean value: ",standard_der_value)
        else:
            x, fx = Minimalization.optimize(functionType, method, coeff, startingPoint, conditions)
            
            print("position:\n",x)
            print("value at\n", x, " : ", fx)

    elif startingPointType == StartingPointType.RANDOM:
        uniformDistributionRange = getRangeOfUniformDistribution()
        if restartMode.isEnabled:
            mean_x, standard_der_x, mean_value, standard_der_value = Minimalization.optimizeRandomRestartMode(restartMode.numOfIterations, functionType, method,
                                                     uniformDistributionRange, coeff, conditions)
            print("mean x: ",mean_x)
            print("standard deriviation from mean x: ",standard_der_x)
            print("mean function value: ",mean_value)
            print("standard deriviation from mean value: ",standard_der_value)
        else:
            x, fx = Minimalization.optimizeRandom(functionType, method, uniformDistributionRange, coeff, conditions)
            
            print("position:\n",x)
            print("value at\n", x, " : ", fx)

if __name__ == '__main__':
    print("*** Gradient Descent ***")
    main()
