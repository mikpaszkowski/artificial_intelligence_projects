import numpy


def fitness_fun(A, b, c, chromosome_ints):
    #here chromosome_ints is already transposed vector/list ->  e.g. [2, 45, 3, 22, 4]
    x_TAx = numpy.dot(numpy.dot(chromosome_ints, A), numpy.transpose(chromosome_ints))
    bx = numpy.dot(numpy.transpose(b), chromosome_ints)
    return x_TAx[0, 0] + bx[0, 0] + c


def roulette_wheel_selection(population, A, b, c, pop_size):
    fitness_arr = [fitness_fun(A, b, c, chromosome) for chromosome in population]
    population_fitness = sum(fitness_arr)
    chromosome_probabilities = fitness_arr / population_fitness
    chromosome_prob_tuples = [(chromosome_probabilities[i], population[i]) for i in
                              range(len(chromosome_probabilities))]

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
