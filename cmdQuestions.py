import numpy
from DistributionRange import DistributionRange
from PyInquirer import prompt
from RestartMode import RestartMode
from ScalarFunCoeff import ScalarFunCoeff
from StopConditions import StopConditions
from VectorFunCoeff import VectorFunCoeff
from enums import MethodType, FunctionType, StartingPointType, StoppingConditionType
from validators import NumberValidator

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
            'default': '10',
            'message': 'Please enter the value of scalar \'c\' coefficient',
            'validate': NumberValidator
        },
        {
            'type': 'input',
            'name': 'b',
            'default': '1;1;1',
            'message': 'Please enter the values of vertcial d-dimensional vector \'b\' coefficient separated by \';\'',

        },
        {
            'type': 'input',

            'name': 'A',
            'default': "1,0,0;0,1,0;0,0,1",
            'message': 'Please enter the values of positivie-definite matrix \'A\' separated by \',\' (row), \';\' (column)',
        }
    ]
    answers = prompt(questions_g)
    return VectorFunCoeff(float(answers['c']), numpy.matrix(answers['b']),
                          numpy.matrix(answers['A']))


def getLearningRate():
    answers = prompt({
        'type': 'input',
        'name': 'learningRate',
        'message': 'Please enter learning rate value',
        'default': '0.001'
    })

    return float(answers['learningRate'])


def getScalarFunctionCoeff():
    answers = prompt([
        {
            'type': 'input',
            'name': 'a',
            'message': 'Please enter value of \'a\' coefficient:',
            'validate': NumberValidator
        },
        {
            'type': 'input',
            'name': 'b',
            'message': 'Please enter value of \'b\' coefficient:',
            'validate': NumberValidator

        },
        {
            'type': 'input',
            'name': 'c',
            'message': 'Please enter value of \'c\' coefficient:',
            'validate': NumberValidator
        },
        {
            'type': 'input',
            'name': 'd',
            'message': 'Please enter value of \'d\' coefficient:',
            'validate': NumberValidator
        }
    ])
    return ScalarFunCoeff(float(answers['a']), float(answers['d']), float(answers['c']), float(answers['d']))


def getStartingPointValue(functionType):
    answer = prompt({
        'type': 'input',
        'name': 'startingPoint',
        'message': 'Please enter the starting point' if functionType == FunctionType.SCALAR else 'Please enter vector of starting points',
        'default': '1' if functionType == FunctionType.SCALAR else '0;1;2',
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

            'message': 'Please enter the \'low\' value of the range for uniform distribution',
            'validate': NumberValidator,

        },
        {
            'type': 'input',
            'name': 'high',
            'message': 'Please enter the \'high\' value of the range for uniform distribution',
            'validate': NumberValidator
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
            'default': '10000',
            'when': lambda answers: answers['stoppingConditionType'] == "Maximal iterations"
        },
        {
            'type': 'input',
            'name': 'desired',
            'message': 'Please enter the desired value to be reached',
            'default': '0.01',
            'when': lambda answers: answers['stoppingConditionType'] == "Desired value",
            'validate': NumberValidator
        },
        {
            'type': 'input',
            'name': 'timeout',
            'message': 'Please enter the maximal computation timeout (seconds)',
            'default': '3',
            'when': lambda answers: answers['stoppingConditionType'] == "Timeout",
            'validate': NumberValidator
        }
    ])
    stoppingConditionType = answers['stoppingConditionType']
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
    if isRestartMode:
        return RestartMode(int(answers['numOfRestarts']), isRestartMode)
    else:
        return RestartMode(0, isRestartMode)
