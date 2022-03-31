import numpy


def mutate_population(population, mut_prob):
    new_pop = []
    for chromosome in population:
        new_pop.append(mutate_chromosome_bitfield(chromosome, mut_prob))
    return new_pop


def mutate_chromosome_bitfield(chromosome_bitfield, mut_prob):
    for i in range(len(chromosome_bitfield)):
        curr_num_bin = numpy.binary_repr(chromosome_bitfield[i])
        mut = mutate_bin(curr_num_bin, mut_prob)
        chromosome_bitfield[i] = convert_bitstring_to_int(mut)
    return chromosome_bitfield


def convert_bitstring_to_int(bit_array):
    return int(''.join(bit_array), 2)


def mutate_bin(curr_num_to_bin, mut_prob):
    mut = []
    for bin_num in curr_num_to_bin:
        if is_mutation_possible(mut_prob):
            if bin_num == "1":
                bin_num = "0"
            elif bin_num == "0":
                bin_num = "1"
            elif bin_num == "-":
                bin_num = " "
        mut.append(bin_num)
    return mut


def is_mutation_possible(mut_prob):
    return numpy.random.uniform(0, 1) <= mut_prob
