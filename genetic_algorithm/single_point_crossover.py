import numpy


def chromosomeCrossover(p1, p2):
    #    print("p1: ", p1)
    #    print("p2: ", p2)

    ch1_bit = []
    ch2_bit = []
    p = []

    size = len(p1)
    crossover_point = numpy.random.randint(1, size)
    for i in range(size):
        if i < crossover_point:
            #    print("p1[i,:]: ", p1[i,:])
            p = p1[i]
            ch1_bit.append(p)
            #  print("ch1: ", ch1_bit)
            ch2_bit.append(p2[i])
        else:
            #    print("p1[i,:]: ", p1[i,:]," p1[i]: ", p1[i])
            ch1_bit.append(p2[i])
            ch2_bit.append(p1[i])
    #    print("p1: ", p1)
    #    print("p2 :", p2)
    #    print("cross over point: ", crossover_point)
    #    print("ch1: ", ch1_bit)
    #    print("ch2: ", ch2_bit)
    #    print ("chromosomeCrossover output: ", ch1_bit, ch2_bit)
    return ch1_bit, ch2_bit


def tuples(population):
    size = len(population)
    parents = []
    #    i = 0
    while size > 0:
        #        i = i+1
        #        print (i)
        p1 = population[0]
        #        print("pre numpy delete population:")
        #        print(population)
        population = numpy.delete(population, 0, axis=0)  # population.pop(0)#
        #        print("post numpy delete population:")
        #        print(population)
        p2_index = numpy.random.randint(0, size - 1)
        p2 = population[p2_index]
        population = numpy.delete(population, p2_index, axis=0)  # population.pop(p2_index)
        #        print("p1: ", p1,"\np2: ", p2)
        parents.append((p1, p2))
        size = size - 2
    #    print("Parent Tuples: ", parents)
    return parents


def crossover(population, crossoverProbability):
    nextGen = []
    if len(population) % 2 != 0:
        randomParent = population.pop(numpy.random.randint(0, len(population) - 1))
        print(randomParent)
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

    print("nextGen: ", nextGen)
    return nextGen
