from collections import defaultdict
import random

class sentencePredict:
    def __init__ (self):
        self.markov = defaultdict(list)
        self.order = 3

    def learn(self, file):
        with open(file,'r') as f:
            inp = f.read()
            inp = inp.lower()
            inp = inp.split('\n')
            for i in range(len(inp)):
                inp[i] = inp[i].split(' ')

            for a in inp:
                for x in a:
                    if a.index(x) > 0:
                        for y in range(1, self.order + 1):
                            if a.index(x) >= y:
                                key = ''
                                for i in range(y):
                                    key += a[a.index(x) - y + i] + ' '

                                self.markov[key[:-1]].append(x)

    def predict(self, inp):
        inp = inp.split(' ')
        lis = []
        for y in range(0, self.order):
            if len(inp) - 1 >= y:
                key = inp[len(inp)-1] + ' '
                for i in range(y):
                    key += inp[len(inp)-1 - y + i] + ' '

                if key[:-1] in self.markov:
                    lis += self.markov[key[:-1]]

        if len(lis) > 0: 
            inp.append(max(set(lis), key = lis.count))

        return ' '.join(inp)

hmm = sentencePredict()