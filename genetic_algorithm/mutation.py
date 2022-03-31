import numpy

from binConverters import intToBin, binToInt


def mutate_population(population, mut_prob):
    new_pop = []
    for chromosome in population:
        new_pop.append(mutate_chromosome_bitfield(chromosome, mut_prob))
    return new_pop

# 1 [23, 55, 46, -23]
#

def mutate_chromosome_bitfield(chromosome_bitfield, mut_prob):
    for i in range(len(chromosome_bitfield)):
        curr_num = chromosome_bitfield[i] # 12
        curr_num_to_bin = numpy.binary_repr(curr_num)
        j = 0
        mut = []
        for bin_num in curr_num_to_bin:
            if is_mutation_possible(mut_prob):
                if bin_num == "1":
                    bin_num = "0"
                elif bin_num == "0":
                    bin_num = "1"
                elif bin_num == "-":
                    bin_num = " "
            mut.append(bin_num) # ["1", "0", "0", "0"]
        chromosome_bitfield[i] = int(''.join(mut), 2)
    return chromosome_bitfield


def is_mutation_possible(mut_prob):
    return numpy.random.uniform(0, 1) <= mut_prob
