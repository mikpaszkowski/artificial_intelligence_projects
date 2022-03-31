import numpy

from mutation import mutate_population
from population import generate_population
from roulette_wheel_selection import fitness_fun, roulette_wheel_selection
from single_point_crossover import crossover


def run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob, iter_num):
    population = generate_population(int_range, pop_size, dim)
    # print(numpy.array(population).tolist())
    minimum = 9999999999999
    for i in range(iter_num):
        # print("\niteration: ", i)
        # selected_population = []
        # crossover_population = []
        # mutated_population = []
        # print("selected")
        selected_population = roulette_wheel_selection(population, matrix_A, vector_b, c, pop_size)
        # print(numpy.array(selected_population).tolist())
        # print("crossover")
        crossover_population = crossover(selected_population, cross_prob)
        # print(numpy.array(crossover_population).tolist())
        # print("mutation")
        mutated_population = mutate_population(crossover_population, mut_prob)
        # print(numpy.array(mutated_population).tolist())
        population = mutated_population
        # if currMinimum < minimum:
        #     minimum = currMinimum
        #     minimum_population = population
        
    # print(mutated_population)
    population_values = []
    for chromosome in population:
        population_values.append(fitness_fun(matrix_A, vector_b, c, chromosome))
    # minimum_population_values = []
    # for chromosome in minimum_population:
    #     minimum_population_values.append(fitness_fun(matrix_A, vector_b, c, chromosome))

    return population, population_values
