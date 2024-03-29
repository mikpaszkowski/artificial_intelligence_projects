from mutation import mutate_population
from population import generate_population
from roulette_wheel_selection import fitness_fun, roulette_wheel_selection
from single_point_crossover import crossover


def run(matrix_A, vector_b, c, dim, int_range, pop_size, cross_prob, mut_prob, iter_num):
    population = generate_population(int_range, pop_size, dim)
    for i in range(iter_num):
        selected_population = roulette_wheel_selection(population, matrix_A, vector_b, c, pop_size)
        crossover_population = crossover(selected_population, cross_prob)
        mutated_population = mutate_population(crossover_population, mut_prob)
        population = mutated_population

    population_values = [fitness_fun(matrix_A, vector_b, c, chromosome) for chromosome in population]

    return population, population_values
