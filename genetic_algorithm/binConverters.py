def intToBin(n, numOfBits=0):
    if numOfBits == 0:
        maximum = max(n)
        minimum = min(n)
        if -minimum > maximum:
            maximum = -minimum

        # print("maximum", maximum)
        numOfBits = 0
        while maximum > 2 ** numOfBits:
            numOfBits = numOfBits + 1
        numOfBits = numOfBits + 1
        # print("numOfBits", numOfBits)
    ret = []
    j = 0
    for i in n:
        if i >= 0:
            ret.append([int(digit) for digit in
                        bin(i)[2:]])  # https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
            while len(ret[j]) < numOfBits - 1:
                ret[j].insert(0, 0)
            while len(ret[j]) > numOfBits - 1:
                ret[j].pop(0)
            ret[j].insert(0, 0)
        else:
            i = -i
            arr = [int(digit) for digit in
                   bin(i)[2:]]  # https://stackoverflow.com/questions/10321978/integer-to-bitfield-as-a-list
            for k in range(len(arr)):
                if arr[k] == 0:
                    arr[k] = 1
                else:
                    arr[k] = 0
            ret.append(arr)
            while len(ret[j]) < numOfBits - 1:
                ret[j].insert(0, 1)
            while len(ret[j]) > numOfBits - 1:
                ret[j].pop(0)
            ret[j].insert(0, 1)

        j = j + 1
    return ret


def binToInt(n):
    out = []
    for i in range(len(n)):
        o = 0  # https://stackoverflow.com/questions/12461361/bits-list-to-integer-in-python
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
