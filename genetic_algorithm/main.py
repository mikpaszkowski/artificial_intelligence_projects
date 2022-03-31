import algorithm
from ui import get_main_parameters, welcome_message, get_function_coeff_and_dim

if __name__ == '__main__':
    welcome_message()

    matrix_A, vector_b, c, dim = get_function_coeff_and_dim()
    int_range, pop_size, cross_prob, mut_prob, iter_num = get_main_parameters()

    print("Processing ...")

    population, population_values = algorithm.run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob,
                                                  iter_num)
    print()
    print("Last population:")
    print(population)
    print()
    print("Last population function values:")
    print(population_values)
    print()
