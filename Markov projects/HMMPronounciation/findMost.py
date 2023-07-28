from collections import defaultdict
import heapq

d = defaultdict(int)
minLen = 3

with open('nonformatWords.txt') as f:
    lines = f.readlines()
    for i in lines:
        length = len(i)
        if length >= minLen:
            for a in range(0, length - minLen):
                for b in range(a + minLen, length):
                    d[i[a:b]] += (b-a)

print(heapq.nlargest(40, d, key=d.get))