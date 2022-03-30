import numpy


def generate_population(int_range, pop_size, dimension):
    population = []
    for _ in range(pop_size):
        phenotype = numpy.random.randint(- 2 ** int_range, 2 ** int_range, dimension)
        population.append(phenotype)
    return numpy.asarray(population)
