import numpy


def intToBit(n):#https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
    return [int(digit) for digit in bin(n)[2:]] # [2:] to chop off the "0b" part 

def bitToInt(bitlist):#https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
    out = 0
    for bit in bitlist:
        out = (out << 1) | bit
    return out

def chromosomeCrossover(p1,p2):

    ch1_bit = []
    ch2_bit = []
    
    size = len(p1)
    crossover_point = numpy.random.randint(1,size)
    for i in range(size):
        if (i < crossover_point):
            ch1_bit.append(p1[i])
            ch2_bit.append(p2[i])
        else:
            ch1_bit.append(p2[i])
            ch2_bit.append(p1[i])
#    print("p1: ", p1)
#    print("p2 :", p2)
#    print("cross over point: ", crossover_point)
#    print("ch1: ", ch1_bit)
#    print("ch2: ", ch2_bit)

    return ch1_bit, ch2_bit

def tuples(population):
    size = len(population)
    parents = []
#    i = 0
    while size > 0:
#        i = i+1
#        print (i)
        p1 = population[0]
        population.pop(0)
        p2_index = numpy.random.randint(0,size-1)
        p2 = population[p2_index]
        population.pop(p2_index)
        parents.append((p1,p2))
        size = size-2
    
    return parents

def crossover(population, crossoverProbability):
    nextGen = []
    if(len(population)%2!=0):
        randomParent = population.pop(numpy.random.randint(0,len(population)-1))
        nextGen.append(randomParent)
    parentTuples = tuples(population)
    for pair in parentTuples:
        if numpy.random.randint(0,1) < crossoverProbability:
            ch1, ch2 = chromosomeCrossover(pair[0], pair[1])
            nextGen.append(ch1)
            nextGen.append(ch2)
        else:
            nextGen.append(pair[0])
            nextGen.append(pair[1])
    
    print("nextGen: ", nextGen)
    return nextGen
