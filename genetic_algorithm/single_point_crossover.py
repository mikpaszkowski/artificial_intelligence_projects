import numpy


def chromosomeCrossover(p1, p2):

    ch1_bit = []
    ch2_bit = []
    p = []

    size = len(p1)
    crossover_point = numpy.random.randint(1, size)
    for i in range(size):
        if i < crossover_point:
            p = p1[i]
            ch1_bit.append(p)
            ch2_bit.append(p2[i])
        else:
            ch1_bit.append(p2[i])
            ch2_bit.append(p1[i])
    return ch1_bit, ch2_bit


def tuples(population):
    size = len(population)
    parents = []
    while size > 0:
        p1 = population[0]
        population = numpy.delete(population, 0, axis=0)  
        p2_index = numpy.random.randint(0, size - 1)
        p2 = population[p2_index]
        population = numpy.delete(population, p2_index, axis=0)  
        parents.append((p1, p2))
        size = size - 2
    return parents


def crossover(population, crossoverProbability):
    nextGen = []
    if len(population) % 2 != 0:
        randomParent = population.pop(numpy.random.randint(0, len(population) - 1))
        nextGen.append(numpy.array(randomParent).tolist())
    parentTuples = tuples(population)
    for pair in parentTuples:
        if numpy.random.randint(0, 1) < crossoverProbability:
            ch1, ch2 = chromosomeCrossover(pair[0], pair[1])
            nextGen.append(ch1)
            nextGen.append(ch2)
        else:
            nextGen.append(pair[0])
            nextGen.append(pair[1])

    return nextGen
