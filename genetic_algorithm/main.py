import algorithm
from population import generate_population
from roulette_wheel_selection import roulette_wheel_selection
from ui import get_function_coeff, get_main_parameters

if __name__ == '__main__':
    matrix_A, vector_b, c = get_function_coeff()
    dim, int_range, pop_size, cross_prob, mut_prob, iter_num = get_main_parameters()
    algorithm.run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob, iter_num)
    # array1 = [1, 1, 0, 1]
    # array2 = [1, 1, 1, 1]
    # population = generate_population(7, 5, 5)
    # print(roulette_wheel_selection(population, matrix_A,
    #                                    vector_b, 1, 5))
