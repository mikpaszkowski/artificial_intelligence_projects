import numpy

def bitfield(n):
    return [int(digit) for digit in bin(n)[2:]] # [2:] to chop off the "0b" part

def intToBin(n, numOfBits = 0):
    if numOfBits == 0:
        maximum = max(n)
        minimum = min(n)
        if(-minimum>maximum):
            maximum = -minimum
        
        print ("maximum", maximum)
        numOfBits = 0
        while(maximum > 2** numOfBits):
            numOfBits = numOfBits+1
        numOfBits = numOfBits +1
        print("numOfBits", numOfBits)
    ret = []
    j = 0
    for i in n:
        if i >= 0:
            ret.append([int(digit) for digit in bin(i)[2:]]) #https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
            while(len(ret[j])<numOfBits-1):
                ret[j].insert(0,0)
            while(len(ret[j])>numOfBits-1):
                ret[j].pop(0)
            ret[j].insert(0,0)
        else:
            i = -i
            arr = [int(digit) for digit in bin(i)[2:]] #https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
            for k in range(len(arr)):
                if arr[k] == 0:
                    arr[k] = 1
                else:
                    arr[k] = 0
            ret.append(arr)
            while(len(ret[j])<numOfBits-1):
                ret[j].insert(0,1)
            while(len(ret[j])>numOfBits-1):
                ret[j].pop(0)
            ret[j].insert(0,1)


        j=j+1
    return  ret

def binToInt(n):
    out = []
    for i in range(len(n)):
        o = 0                   #https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
        if n[i][0] == 0:
            for bit in n[i]:
                o = (o << 1) | bit
            
        else:
            for bit in n[i]:
                if bit == 1:
                    bit = 0
                else:
                    bit = 1
                o = (o << 1) | bit
            o = -o
        out.append(o)

    return out

def chromosomeCrossover(p1,p2):
#    print("p1: ", p1)
#    print("p2: ", p2)

    ch1_bit = []
    ch2_bit = []
    p = []
    
    size = len(p1)
    crossover_point = numpy.random.randint(1,size)
    for i in range(size):
        if (i < crossover_point):
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
        population = numpy.delete(population, 0, axis = 0) #population.pop(0)#
#        print("post numpy delete population:")
#        print(population)
        p2_index = numpy.random.randint(0,size-1)
        p2 = population[p2_index]
        population = numpy.delete(population, p2_index, axis = 0)#population.pop(p2_index)
#        print("p1: ", p1,"\np2: ", p2)
        parents.append((p1,p2))
        size = size-2
#    print("Parent Tuples: ", parents)
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
