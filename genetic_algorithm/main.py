import numpy

import algorithm
from population import generate_population
from roulette_wheel_selection import roulette_wheel_selection
from ui import get_function_coeff, get_main_parameters

if __name__ == '__main__':
    matrix_A, vector_b, c = get_function_coeff()
    dim, int_range, pop_size, cross_prob, mut_prob, iter_num = get_main_parameters()
    population, population_values = algorithm.run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob, iter_num)
    print("last population:")
    print(population)
    print("last population values:")
    print(population_values)

