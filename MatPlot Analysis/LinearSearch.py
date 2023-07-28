from random import randint
def linSearch(data, find = randint(-120,120)):
    outP = 'NaN'

    for n in data:
        if n == find:
            return n

    return outP

