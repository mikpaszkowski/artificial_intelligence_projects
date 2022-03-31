import numpy


def fitness_fun(A, b, c, chromosome_ints):
    x_TAx = numpy.dot(numpy.dot(chromosome_ints, A), numpy.transpose(chromosome_ints))
    bx = numpy.dot(numpy.transpose(b), chromosome_ints)
    return x_TAx[0, 0] + bx[0, 0] + c


def roulette_wheel_selection(population, A, b, c, pop_size):
    print("population fitness")
    population_fitness = sum([fitness_fun(A, b, c, chromosome) for chromosome in population])
    print(population_fitness)
    print(max([fitness_fun(A, b, c, chromosome) for chromosome in population]))
    print(min([fitness_fun(A, b, c, chromosome) for chromosome in population]))
    # if population_fitness != 0:
    chromosome_probabilities = [fitness_fun(A, b, c, chromosome) / population_fitness for chromosome in
                                    population]
    # else:
    #     chromosome_probabilities = [fitness_fun(A, b, c, chromosome) / 0.01 for chromosome in
    #                                 population]
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
