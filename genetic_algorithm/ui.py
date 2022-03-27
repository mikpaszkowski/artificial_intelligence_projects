from PyInquirer import prompt
import numpy

from validators import SymmetricMatrixValidator, VectorValidator, NumberValidator, IntegerValidator, \
    PositiveIntegerValidator, ProbabilityValidator


def get_function_coeff():
    answer_a = prompt(
        {
            'type': 'input',
            'name': 'A',
            'message': "Please enter the values of {n}x{n} positivie-definite matrix \'A\' separated by \',\' (row), \';\' (column):",
            'validate': SymmetricMatrixValidator
        })

    matrix_A = numpy.matrix(answer_a['A'])
    a_b_dim_equals = False

    while not a_b_dim_equals:
        answer_b = prompt({
            'type': 'input',
            'name': 'b',
            'message': 'Please enter the values of n-length vector b, each separated by \',\' (i.e. 1,2,3,4,5):',
            'validate': VectorValidator
        })
        if numpy.array(answer_b['b']).size == matrix_A.shape[0]:
            a_b_dim_equals = True

        print('Length of vector b should be the same as size of matrix A n x n:')

    answer_c = prompt({
        'type': 'input',
        'name': 'c',
        'message': 'Please enter the value of scalar \'c\' coefficient:',
        'validate': NumberValidator
    })

    return matrix_A, numpy.array(answer_b['b']), float(answer_c['c'])


def get_main_parameters():
    answers = prompt(
        {
            'type': 'input',
            'name': 'dimension',
            'message': "Please enter the value of problem dimensionality:",
            'validate': IntegerValidator
        },
        {
            'type': 'input',
            'name': 'integer_range',
            'message': "Please enter the range value of searched integers d >= 1:",
            'validate': PositiveIntegerValidator
        },
        {
            'type': 'input',
            'name': 'population_size',
            'message': "Please enter the value of population size:",
            'validate': IntegerValidator
        },
        {
            'type': 'input',
            'name': 'crossover_probability',
            'message': "Please enter the value of crossover probability:",
            'validate': ProbabilityValidator
        },
        {
            'type': 'input',
            'name': 'mutation_probability',
            'message': "Please enter the value of mutation probability:",
            'validate': ProbabilityValidator
        },
        {
            'type': 'input',
            'name': 'iterations_num',
            'message': 'Please enter the value of iterations:',
            'validate': IntegerValidator
        }
    )

    return int(answers['dimension']), int(answers('integer_range')), int(answers('population_size')), \
           float(answers['crossover_probability']), float(answers['mutation_probability']), int(answers['iterations_num'])
