from __future__ import print_function, unicode_literals

from Minimalization import Minimalization
from cmdQuestions import getMethodAndFunctionType, getStartingPointType, getScalarFunctionCoeff, getStoppingConditions, \
    getNumOfRestartMode, getStartingPointValue, getRangeOfUniformDistribution, getVectorFunctionCoeff, \
    StartingPointType, MethodType, FunctionType
import numpy

def main():
    method, functionType = getMethodAndFunctionType()

    startingPointType = getStartingPointType()

    if functionType == FunctionType.SCALAR:
        scalarCoeff = getScalarFunctionCoeff()
        conditions = getStoppingConditions()
        restartMode = getNumOfRestartMode()

        if startingPointType == StartingPointType.MANUAL:
            startingPoint = getStartingPointValue(functionType)
            Minimalization.gradientDescent_F(method, scalarCoeff, startingPoint, conditions)

        elif startingPointType == StartingPointType.RANDOM:
            uniformDistributionRange = getRangeOfUniformDistribution()
            Minimalization.gradientDescentRandom(functionType, method, uniformDistributionRange, scalarCoeff,
                                                 conditions)

    elif functionType == FunctionType.VECTOR:
        vectorCoeff = getVectorFunctionCoeff()
        conditions = getStoppingConditions()
        numOfRestarts = getNumOfRestartMode()
        if startingPointType == StartingPointType.MANUAL:
            startingPoint = getStartingPointValue(functionType)
            l = numpy.dot(numpy.transpose(startingPoint), numpy.dot(vectorCoeff.A, startingPoint))
            print(numpy.dot(numpy.transpose(startingPoint), numpy.dot(vectorCoeff.A, startingPoint)))
            Minimalization.gradientDescent_G(method, vectorCoeff, startingPoint, conditions)
        elif startingPointType == StartingPointType.RANDOM:
            uniformDistributionRange = getRangeOfUniformDistribution()
            Minimalization.gradientDescentRandom(functionType, method, uniformDistributionRange, vectorCoeff,
                                                 conditions)


if __name__ == '__main__':
    print("*** Gradient Descent ***")
    main()
