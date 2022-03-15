import time

from helpers import *
from enums import *


def isTimeoutReached(startTime, stopConditions):
    return stopConditions.type == StoppingConditionType.TIMEOUT and time.time() - startTime >= stopConditions.value


def isDesiredValueReached_G(coeff, stopConditions, x):
    return stopConditions.type == StoppingConditionType.DESIRED_VALUE and function_G(coeff, x).item(
        0) <= stopConditions.value


def isDesiredValueReached_F(coeff, stopConditions, x):
    return stopConditions.type == StoppingConditionType.DESIRED_VALUE and function_F(coeff, x) <= stopConditions.value


def isIterationNumberReached(currIteration, stopConditions):
    return stopConditions.type == StoppingConditionType.ITERATIONS and currIteration == stopConditions.value - 1


def checkConditions_G(stopConditions, coeff, startTime, currNumOfIterations, x):
    if isTimeoutReached(startTime, stopConditions):
        return True, "Terminated by Timeout stop condition"
    elif isIterationNumberReached(currNumOfIterations, stopConditions):
        return True, 'Terminated by number of iterations stop condition'
    elif isDesiredValueReached_G(coeff, stopConditions, x):
        return True, "Terminated by desired value stop condition"
    else:
        return False, ""


def checkConditions_F(stopConditions, coeff, startTime, currNumOfIterations, x):
    if isTimeoutReached(startTime, stopConditions):
        return True, "Terminated by Timeout stop condition"
    elif isIterationNumberReached(currNumOfIterations, stopConditions):
        return True, 'Terminated by number of iterations stop condition'
    elif isDesiredValueReached_F(coeff, stopConditions, x):
        return True, "Terminated by desired value stop condition"
    else:
        return False, ""
