from __future__ import print_function, unicode_literals

from cmdQuestions import getMethodAndFunctionType, getStartingPointType, getScalarFunctionCoeff, getStoppingConditions, \
    getNumOfRestartMode, getStartingPointValue, getRangeOfUniformDistribution, getVectorFunctionCoeff, getStartingVectorValue, StartingPointType
from gradient_descent import optimalisationF, optimalisationFRandom, optimalisationFRandomN, optimalisationG, optimalisationGRandom, optimalisationGRandomN
# zmiany:
#   nazwa gradientDescent zmieniona na optimisationF
#   nazwy gradientDescentRandom i gradientDescentRandomN tak samo zmienione
#   dodano zmienną type do wszystkich funkcji
#   Funkcja getVectorFunctionCoeff zaimplementowana
#   Funkcje optimalisationFRandom i optimalisationFRandomN zaimplemelntowane
#   dadana funkcja getStartingVectorValue 
#   Funkcje optimalisationGRandom i optimalisationGRandomN zaimplemelntowane
#
# ToDo:
#   naprawić funkcje newtona dla G(x)
#
#

def main():
    method, functionType = getMethodAndFunctionType()

    startingPointType = getStartingPointType()

    # tutaj w chuj powtórzeń kodu ale tak zostawiłem aby było wiadomo jakie przypadki rozpatrujemy

    #Dzięki zmiennej type ten kod nie musi się powtarzać
    if method == 'Gradient Descent': 
        type = "g"
    elif method == 'Newton\'s':
        type = "n"
    if functionType == 'F(x)':
        scalarCoeff = getScalarFunctionCoeff()
        conditions = getStoppingConditions()
        numOfRestarts = getNumOfRestartMode()

        if numOfRestarts == 1:
            if startingPointType == StartingPointType.MANUAL:
                startingPoint = getStartingPointValue()
                optimalisationF(type, scalarCoeff, startingPoint, conditions) 

            elif startingPointType == StartingPointType.RANDOM:
                uniformDistributionRange = getRangeOfUniformDistribution()
                optimalisationFRandom(type, uniformDistributionRange, scalarCoeff, conditions)
        elif numOfRestarts > 1:
            uniformDistributionRange = getRangeOfUniformDistribution()
            optimalisationFRandomN(type, numOfRestarts, uniformDistributionRange, scalarCoeff, conditions)

    elif functionType == 'G(x)':
        print("a")
        vectorCoeff = getVectorFunctionCoeff()
        conditions = getStoppingConditions()
        numOfRestarts = getNumOfRestartMode()
        if numOfRestarts == 1:
            print("b")
         #   print("starting point type: ", startingPointType)
            if startingPointType == StartingPointType.MANUAL:
                print("c")
                startingPoint = getStartingVectorValue(len(vectorCoeff.b))
                optimalisationG(type, vectorCoeff, startingPoint, conditions)
            elif startingPointType == StartingPointType.RANDOM:
                print("d")
                uniformDistributionRange = getRangeOfUniformDistribution()
                optimalisationGRandom(type, uniformDistributionRange, vectorCoeff, conditions)
        elif numOfRestarts > 1:
            print("e")
            uniformDistributionRange = getRangeOfUniformDistribution()
            optimalisationGRandomN(type, numOfRestarts, uniformDistributionRange, vectorCoeff, conditions)

#    elif method == 'Newton':
#        if functionType == 'F(x)':
#            scalarCoeff = getScalarFunctionCoeff()
#            conditions = getStoppingConditions()
#            numOfRestarts = getNumOfRestartMode()
#
#            if startingPointType == StartingPointType.MANUAL:
#
#                startingPoint = getStartingPointValue()
#                optimalisationF(scalarCoeff, startingPoint, conditions)
#
#            elif startingPointType == StartingPointType.RANDOM:
#
#                uniformDistributionRange = getRangeOfUniformDistribution()
#                optimalisationFRandom(uniformDistributionRange, scalarCoeff, conditions)
#
#        elif functionType == 'G(x)':
#            vectorCoeff = getVectorFunctionCoeff()
            # conditions = getStoppingConditions()
            # numOfRestarts = getNumOfRestartMode()
            # if startingPointType == 'Defined Manually':
            #     startingPoint = getStartingPointValue()
            #     optimalisationF(scalarCoeff, startingPoint, conditions)
            # elif startingPointType == 'Randomly generated':
            #     uniformDistributionRange = getRangeOfUniformDistribution()
            #     optimalisationFRandom(uniformDistributionRange, scalarCoeff, conditions)


if __name__ == '__main__':
    print("*** Gradient Descent ***")
    main()
