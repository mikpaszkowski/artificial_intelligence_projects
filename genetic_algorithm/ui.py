import numpy
from PyInquirer import prompt

from validators import SymmetricMatrixValidator, VectorValidator, NumberValidator, IntegerValidator, \
    PositiveIntegerValidator, ProbabilityValidator


def get_function_coeff():
    answer_a = prompt(
        {
            'type': 'input',
            'name': 'A',
            'message': "Please enter the values of {n}x{n} positivie-definite matrix \'A\' separated by \',\' (row), \';\' (column):",
            'default': '1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;1,1,1,1,1;1,1,1,1,1',
            'validate': SymmetricMatrixValidator
        })

    matrix_A = numpy.matrix(answer_a['A'])
    a_b_dim_equals = False

    while not a_b_dim_equals:
        answer_b = prompt({
            'type': 'input',
            'name': 'b',
            'message': 'Please enter the values of n-length vector b, each separated by \';\' (i.e. 1;2;3;4;5):',
            'default': '1;2;3;4;5',
            'validate': VectorValidator
        })
        if numpy.matrix(answer_b['b']).size == matrix_A.shape[0]:
            a_b_dim_equals = True
        else:
            print('Length of vector b should be the same as size of matrix A n x n:')

    answer_c = prompt({
        'type': 'input',
        'name': 'c',
        'message': 'Please enter the value of scalar \'c\' coefficient:',
        'default': "1",
        'validate': NumberValidator
    })

    return matrix_A, numpy.matrix(answer_b['b']), float(answer_c['c'])


def get_main_parameters():
    answer_dim = prompt(
        {
            'type': 'input',
            'name': 'dimension',
            'message': "Please enter the value of problem dimensionality:",
            'validate': IntegerValidator
        })
    answer_int_range = prompt(
        {
            'type': 'input',
            'name': 'integer_range',
            'message': "Please enter the range value of searched integers d >= 1:",
            'validate': PositiveIntegerValidator
        }
    )
    answer_cross_prob = prompt(
        {
            'type': 'input',
            'name': 'cross_prob',
            'message': "Please enter the value of crossover probability:",
            'validate': ProbabilityValidator
        })

    answer_mut_prob = prompt(
        {
            'type': 'input',
            'name': 'mut_prob',
            'message': "Please enter the value of mutation probability:",
            'validate': ProbabilityValidator
        }
    )
    answer_pop_size = prompt(
        {
            'type': 'input',
            'name': 'pop_size',
            'message': "Please enter the value of population size:",
            'validate': IntegerValidator
        })

    answer_iter_num = prompt(
        {
            'type': 'input',
            'name': 'iter_num',
            'message': 'Please enter the value of iterations:',
            'validate': IntegerValidator
        }
    )

    return int(answer_dim['dimension']), int(answer_int_range['integer_range']), int(answer_pop_size['pop_size']), float(answer_cross_prob['cross_prob']), float(answer_mut_prob['mut_prob']), int(answer_iter_num['iter_num'])
