from random import randint
from selectSort import selectSort
from mergeSort import mergeSort

def binSearch(data, sorter, find = randint(-110,110)):
    data = sorter(data)

    outP = 'NaN'

    i = round((len(data)-1)/2)
    c = round((len(data)-1)/4)
    o = False
    while True:
        if data[i] > find:
            i -= c
            
        elif data[i] < find:
            i += c

        else:
            outP = data[i]
            break
            
        if o or c == 0:
            break

        if c == 1:
            o = True
        
        c = round(c/2)

    return outP

def sortedBinSearch(data,find = randint(-120,120)):
    outP = 'NaN'

    i = round((len(data)-1)/2)
    c = round((len(data)-1)/4)
    o = False
    while True:
        if data[i] > find:
            i -= c
            
        elif data[i] < find:
            i += c

        else:
            outP = data[i]
            break
            
        if o or c == 0:
            break

        if c == 1:
            o = True
        
        c = round(c/2)

    return outP

def selectBinSearch(data, find = randint(-110,110)):
    return binSearch(data,selectSort,find)

def mergeBinSearch(data, find = randint(-110,110)):
    return binSearch(data,mergeSort,find)

def pysortBinSearch(data, find = randint(-110,110)):
    return binSearch(data,sorted,find)

if __name__ == "__main__":
    print(pysortBinSearch([1],1))