import numpy

from mutation import mutate_population
from population import generate_population
from roulette_wheel_selection import roulette_wheel_selection
from single_point_crossover import crossover


def run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob, iter_num):
    population = generate_population(int_range, pop_size, dim)
    print(numpy.array(population).tolist())
    for i in range(iter_num):
        # print("selected")
        selected_population = roulette_wheel_selection(population, matrix_A, vector_b, c, pop_size)
        # print(numpy.array(selected_population).tolist())
        # print("crossover")
        crossover_population = crossover(selected_population, cross_prob)
        # print(numpy.array(crossover_population).tolist())
        # print("mutation")
        mutated_population = mutate_population(crossover_population, mut_prob)
        # print(numpy.array(mutated_population).tolist())
    print(mutated_population)
