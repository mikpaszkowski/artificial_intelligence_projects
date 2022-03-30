import numpy


def mutate_population(population, mut_prob):
    new_pop = []
    for chromosome in population:
        new_pop.append(mutate_chromosome_bitfield(chromosome, mut_prob))
    return new_pop


def mutate_chromosome_bitfield(chromosome_bitfield, mut_prob):
    for i in range(len(chromosome_bitfield)):
        curr_bit = chromosome_bitfield[i]
        if is_mutation_possible(mut_prob):
            if curr_bit == 1:
                chromosome_bitfield[i] = 0
            else:
                chromosome_bitfield[i] = 1
    return chromosome_bitfield


def is_mutation_possible(mut_prob):
    return numpy.random.uniform(0, 1) <= mut_prob
