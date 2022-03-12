from enum import Enum, unique

import numpy
from PyInquirer import prompt

from DistributionRange import DistributionRange
from RestartMode import RestartMode
from ScalarFunCoeff import ScalarFunCoeff
from StopConditions import StopConditions
from VectorFunCoeff import VectorFunCoeff
from validators import CoefficientValidator


@unique
class MethodType(Enum):
    GRADIENT_DESCENT = 'Gradient Descent'
    NEWTON = 'Newton'

    def fromString(value):
        if value == 'Gradient Descent':
            return MethodType.GRADIENT_DESCENT
        elif value == 'Newton':
            return MethodType.NEWTON
        else:
            raise TypeError("There is enum of type ", value)


@unique
class StartingPointType(Enum):
    MANUAL = 'Defined manually',
    RANDOM = 'Randomly generated'

    def fromString(value):
        if value == 'Defined manually':
            return StartingPointType.MANUAL
        elif value == 'Randomly generated':
            return StartingPointType.RANDOM
        else:
            raise TypeError("There is enum of type ", value)


@unique
class FunctionType(Enum):
    SCALAR = 'F(x)'
    VECTOR = 'G(x)'

    def fromString(value):
        if value == 'F(x)':
            return FunctionType.SCALAR
        elif value == 'G(x)':
            return FunctionType.VECTOR
        else:
            raise TypeError("There is enum of type ", value)


@unique
class StoppingConditionType(Enum):
    ITERATIONS = 'Maximal iterations',
    DESIRED_VALUE = "Desired value",
    TIMEOUT = "Timeout"

    def fromString(value):
        if value == 'Maximal iterations':
            return StoppingConditionType.ITERATIONS
        elif value == "Desired value":
            return StoppingConditionType.DESIRED_VALUE
        elif value == "Timeout":
            return StoppingConditionType.TIMEOUT
        else:
            raise TypeError("There is enum of type ", value)


def getMethodAndFunctionType():
    answers = prompt([
        {
            'type': 'list',
            'name': 'method',
            'message': 'What method of function minimization do you want?',
            'choices': ['Gradient Descent', 'Newton']
        },
        {
            'type': 'list',
            'name': 'function_type',
            'message': 'What function type should be optimized? (F(x) = ax^3 + bx^2 + cx +d, G(x) = c + b^Tx + x^TAx)',
            'choices': ['F(x)', 'G(x)']
        }
    ])
    return MethodType.fromString(answers['method']), FunctionType.fromString(answers['function_type'])


def getVectorFunctionCoeff():
    questions_g = [
        {
            'type': 'input',
            'name': 'c',
            'default': '1',
            'message': 'Please enter the value of scalar \'c\' coefficient',
            'validate': CoefficientValidator
        },
        {
            'type': 'input',
            'name': 'b',
            'default': '1; 1',
            'message': 'Please enter the values of d-dimensional vector \'b\' coefficient separated by \',\' (row), \';\' (column)',

        },
        {
            'type': 'input',
            'name': 'x',
            'default': '1; 1',
            'message': 'Please enter the values of d-dimensional vector \'x\' coefficient separated by space (row), \';\' (column)',
        },
        {
            'type': 'input',
            'name': 'A',
            'default': "1 1; -1 1",
            'message': 'Please enter the values of positivie-definite matrix \'A\' separated by \',\' (row), \';\' (column)',
        }
    ]
    answers = prompt(questions_g)
    return VectorFunCoeff(float(answers['c']), numpy.matrix(answers['b']), numpy.matrix(answers['x']),
                          numpy.matrix(answers['A']))


def getScalarFunctionCoeff():
    answers = prompt([
        {
            'type': 'input',
            'name': 'a',
            'message': 'Please enter value of \'a\' coefficient:',
            'validate': CoefficientValidator
        },
        {
            'type': 'input',
            'name': 'b',
            'message': 'Please enter value of \'b\' coefficient:',
            'validate': CoefficientValidator

        },
        {
            'type': 'input',
            'name': 'c',
            'message': 'Please enter value of \'c\' coefficient:',
            'validate': CoefficientValidator
        },
        {
            'type': 'input',
            'name': 'd',
            'message': 'Please enter value of \'d\' coefficient:',
            'validate': CoefficientValidator
        }
    ])
    return ScalarFunCoeff(float(answers['a']), float(answers['d']), float(answers['c']), float(answers['d']))


def getStartingPointValue(functionType):
    answer = prompt({
        'type': 'input',
        'name': 'startingPoint',
        'message': 'Please enter the starting point' if functionType == FunctionType.SCALAR else 'Please enter vector of starting points',
        'default': '1',
        # 'validate': CoefficientValidator
    })
    if functionType == FunctionType.SCALAR:
        return float(answer['startingPoint'])
    elif functionType == FunctionType.VECTOR:
        return numpy.matrix(answer['startingPoint'])


def getRangeOfUniformDistribution():
    answer = prompt([
        {
            'type': 'input',
            'name': 'low',
            "message": 'Please enter the \'low\' value of the range for uniform distribution'
        },
        {
            'type': 'input',
            'name': 'high',
            'message': 'Please enter the \'high\' value of the range for uniform distribution'
        }
    ])
    return DistributionRange(float(answer['low']), float(answer['high']))


def getStartingPointType():
    answers = prompt(
        {
            'type': 'list',
            'name': 'startingPointType',
            'message': 'What kind of starting point do you want ?',
            'choices': ['Defined manually', 'Randomly generated']
        }
    )
    return StartingPointType.fromString(answers['startingPointType'])


def getStoppingConditions():
    answers = prompt([
        {
            'type': 'list',
            'name': 'stoppingConditionType',
            'message': 'Please choose stopping condition',
            'choices': ['Maximal iterations', 'Desired value', 'Timeout']
        },
        {
            'type': 'input',
            'name': 'iterations',
            'message': 'Please enter the maximal number of iterations',
            'default': '100',
            'when': lambda answers: answers['stoppingConditionType'] == "Maximal iterations"
            # 'validate': lambda num: float(num) > 0 or 'Value must be bigger than 0!'
        },
        {
            'type': 'input',
            'name': 'desired',
            'message': 'Please enter the desired value to be reached',
            'default': '0.01',
            'when': lambda answers: answers['stoppingConditionType'] == "Desired value"
            # 'validate': lambda val: float(val) > 0.0 or 'Desired value must be a number!'
        },
        {
            'type': 'input',
            'name': 'timeout',
            'message': 'Please enter the maximal computation timeout (seconds)',
            'default': '1000',
            'when': lambda answers: answers['stoppingConditionType'] == "Timeout"
            # 'validate': lambda val: int(val) > 0 or 'Value must be a number bigger than 0!'
        },
        # {
        #     'type': 'input',
        #     'name': 'tolerance',
        #     'message': 'Please enter the minimal tolerance value for termination of process',
        #     'default': '0.0001',
        #     # 'validate': lambda val: float(val) > 0.0 or 'Value must be a number bigger than 0!'
        # }
    ])
    stoppingConditionType = answers['stoppingConditionType']
    # tolerance = float(answers['tolerance'])
    if stoppingConditionType == 'Maximal iterations':
        return StopConditions(float(answers['iterations']), StoppingConditionType.ITERATIONS)
    elif stoppingConditionType == 'Desired value':
        return StopConditions(float(answers['desired']), StoppingConditionType.DESIRED_VALUE)
    else:
        return StopConditions(float(answers['timeout']), StoppingConditionType.TIMEOUT)


def getNumOfRestartMode():
    answers = prompt([
        {
            'type': 'confirm',
            'message': 'Do you want to use batch/restart mode?',
            'name': 'restartMode',
            'default': True
        },
        {
            'type': 'input',
            'name': 'numOfRestarts',
            'message': 'Please enter the number of times the optimization process to be restarted',
            'default': '10',
            'when': lambda answer: answer['restartMode'],
        }
    ])
    isRestartMode = answers['restartMode']
    if isRestartMode == True:
        return RestartMode(answers['numOfRestarts'], isRestartMode)
    else:
        return RestartMode(0, isRestartMode);
