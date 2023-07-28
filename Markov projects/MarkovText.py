from collections import defaultdict
import random

dic = defaultdict(list)
order = 4

for i in range(3,4):
    with open(f'poem{i}.txt','r') as f:
        inp = f.read()
        inp = inp.lower()
        inp = inp.split(' ')

        for x in inp:
            if inp.index(x) > order - 1:
                key = ''
                for i in range(order):
                    key += inp[inp.index(x) - order + i] + ' '

                dic[key[:-1]].append(x)

length = 100
string = []

for i in random.choice(list(dic)).split(' '):
    string.append(i)

x = order
while x < length + 1:
    key = ''
    for i in range(0, order, 1):
        key += string[x - (order - i)] + ' '

    if key[:-1] in dic and len(dic[key[:-1]]) > 0:
        string.append(random.choice(dic[key[:-1]]))
    else:
        for i in random.choice(list(dic)).split(' '):
            string.append(i)
        x += order - 1

    x += 1

with open('new.txt','w+') as f:
    f.write(' '.join(string))
    f.close()