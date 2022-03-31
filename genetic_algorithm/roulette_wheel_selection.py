import numpy


def fitness_fun(A, b, c, chromosome_bitfield):
    x_TAx = numpy.dot(numpy.dot(numpy.transpose(chromosome_bitfield), A), chromosome_bitfield)
    bx = numpy.dot(numpy.transpose(b), chromosome_bitfield)
    return x_TAx + bx + c

def roulette_wheel_selection(population, A, b, c, pop_size):
    population_fitness = sum([fitness_fun(A, b, c, chromosome).item(0, 0) for chromosome in population])
    chromosome_probabilities = [fitness_fun(A, b, c, chromosome).item(0, 0)/population_fitness for chromosome in population]

    chromosome_prob_tuples = [(chromosome_probabilities[i], population[i]) for i in range(len(chromosome_probabilities))]

    wheel = get_roulette_wheel(chromosome_prob_tuples)

    return select_parents_from_wheel(wheel, chromosome_prob_tuples, pop_size)


def select_parents_from_wheel(wheel, chromosome_prob_tuples, pop_size):
    arr = []
    for _ in range(pop_size):
        spin = numpy.random.uniform(0, 1)
        i = 0
        while i in range(len(wheel)) and wheel[i] < spin:
            i += 1
        arr.append(chromosome_prob_tuples[i][1])
    return arr


def get_roulette_wheel(chromosome_prob_tuples):
    arr = []
    prev_prob = 0
    for prob in chromosome_prob_tuples:
        curr_prob = prev_prob + prob[0]
        arr.append(curr_prob)
        prev_prob = curr_prob
    return arr
