from enum import Enum

from PyInquirer import prompt

from ScalarFunCoeff import ScalarFunCoeff
from StopConditions import StopConditions
from VectorFunCoeff import VectorFunCoeff
from validators import CoefficientValidator


class MethodType(Enum):
    GRADIENT_DESCENT = 1
    NEWTON = 2


class StartingPointType(Enum):
    MANUAL = 1,
    RANDOM = 2


class FunctionType(Enum):
    SCALAR = 1,
    VECTOR = 2


def getMethodAndFunctionType():
    promptQuestions = [
        {
            'type': 'list',
            'name': 'method',
            'message': 'What method of function minimization do you want?',
            'choices': ['Gradient Descent', 'Newton\'s']
        },
        {
            'type': 'list',
            'name': 'function_type',
            'message': 'What function type should be optimized? (F(x) = ax^3 + bx^2 + cx +d, G(x) = c + b^Tx + x^TAx)',
            'choices': ['F(x)', 'G(x)']
        }
    ]

    answers = prompt(promptQuestions)
    return answers['method'], answers['function_type']


def getVectorFunctionCoeff():
    questions_g = [
        {
            'type': 'input',
            'name': 'c',
            'message': 'Please enter the value of scalar \'c\' coefficient',
            'validate': CoefficientValidator
        },
        {
            'type': 'input',
            'name': 'b',
            'message': 'Please enter the values of d-dimensional vector \'c\' coefficient separated by comma',

        },
        {
            'type': 'input',
            'name': 'x',
            'message': 'Please enter the values of d-dimensional vector \'x\' coefficient separated by comma',

        }
    ]
    answers = prompt(questions_g)
    return VectorFunCoeff(float(answers['c']), float(answers['b']), float(answers['x']))


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


def getStartingPointValue():
    answer = prompt({
        'type': 'input',
        'name': 'startingPoint',
        'message': 'Please enter the starting point',
        'default': '1',
        'validate': CoefficientValidator
    })
    return float(answer['startingPoint'])


def getRangeOfUniformDistribution():
    answer = prompt([
        {
            'type': 'input',
            'name': 'low',
            "message": 'Please enter the \'low\' value of the range for uniform distribution',
            "when": lambda answers: answers['startingPointType'] == "Randomly generated"
        },
        {
            'type': 'input',
            'name': 'high',
            'message': 'Please enter the \'high\' value of the range for uniform distribution',
            'when': lambda answers: answers['startingPointType'] == 'Randomly generated'
        }
    ])

    return float(answer['low']), float(answer['high'])



def getStartingPointType():
    answers = prompt([
        {
            'type': 'list',
            'name': 'startingPointType',
            'message': 'What kind of starting point do you want ?',
            'choices': ['Defined manually', 'Randomly generated']
        }
    ])
    if answers['startingPointType'] == 'Defined manually':
        return StartingPointType.MANUAL
    else:
        return StartingPointType.RANDOM


def getStoppingConditions():
    answers = prompt([
        {
            'type': 'input',
            'name': 'iterations',
            'message': 'Please enter the maximal number of iterations',
            'default': '100',
            # 'validate': lambda num: float(num) > 0 or 'Value must be bigger than 0!'
        },
        {
            'type': 'input',
            'name': 'desired',
            'message': 'Please enter the desired value to be reached',
            'default': '0.01',
            # 'validate': lambda val: float(val) > 0.0 or 'Desired value must be a number!'
        },
        {
            'type': 'input',
            'name': 'timeout',
            'message': 'Please enter the maximal computation timeout (seconds)',
            'default': '1000',
            # 'validate': lambda val: int(val) > 0 or 'Value must be a number bigger than 0!'
        },
        {
            'type': 'input',
            'name': 'tolerance',
            'message': 'Please enter the minimal tolerance value for termnation of process',
            'default': '0.0001',
            # 'validate': lambda val: float(val) > 0.0 or 'Value must be a number bigger than 0!'
        }
    ])
    return StopConditions(int(answers['iterations']), float(answers['desired']), int(answers['timeout']),
                          float(answers['tolerance']))


def getNumOfRestartMode():
    answer = prompt({
        'type': 'input',
        'name': 'numOfRestarts',
        'message': 'Please enter the number of times the optimization process to be restarted',
        'default': '10',
        'validate': lambda val: (str(val).isdigit() and int(val) > 0) or 'Value must be a number bigger than 0!'
    })
    return int(answer['numOfRestarts'])
