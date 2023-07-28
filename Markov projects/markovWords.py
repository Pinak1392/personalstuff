from combinations import combo
import pickle

class autoCorrect:
    def __init__(self):
        #Hidden States
        self.states = ('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z')
        self.states = combo(self.states,2)

        #The probability of a certain state being a certain observable state
        self.emit_p = {}

        for x in self.states:
            self.emit_p[x] = {}
            for i in self.states:
                self.emit_p[x][i] = [[1/len(self.states) for x in range(10)],len(self.states)]
            
        self.initial = {}
        for x in self.states:
            self.initial[x] = 1

        #The Probability of going from hidden state to next hidden state
        self.trans_p = {}

        for x in self.states:
            self.trans_p[x] = [{}, 0]
            for i in self.states:
                self.trans_p[x][0][i] = 1/len(self.states)

    def viterbi(self, obs):
        obs = list(obs)
        nobs = []
        for x in range(1,len(obs)):
            nobs.append(obs[x-1] + obs[x])
        obs = nobs

        V = [{}]

        if len(obs) == 0:
            return []

        #Sets up the initial probabilities based on the first observed state
        for st in self.states:
            #Finds the overall initial probability by multiplying the probability of event given state by the probability of the state initially
            V[0][st] = {"prob": self.initial[st] * self.emit_p[st][obs[0]][0][0], "prev": None}

        # Run when length of observed is greater than 1
        for t in range(1, len(obs)):

            #Create a new set of probabilities for the next observation
            V.append({})

            for st in self.states:
                #Find the starting maximum probability from the probability of a starting tag given previous tag probability and transition probability
                max_tr_prob = V[t-1][self.states[0]]["prob"]*self.trans_p[self.states[0]][0][st]

                #Stores the selected most probable state 
                prev_st_selected = self.states[0]

                for prev_st in self.states[1:]:
                    #Gets the probability of a state given a previous state chance of transition and its probability
                    tr_prob = V[t-1][prev_st]["prob"]*self.trans_p[prev_st][0][st]

                    #If the found probability is greater than the max probability, change it to the new one
                    if tr_prob > max_tr_prob:

                        max_tr_prob = tr_prob

                        #Also change the probable previous state to the one transitioned from by the new probability
                        prev_st_selected = prev_st

                        
                #Get overall max probability of tag from maximum transition probability and the probability that it emitted the observed state
                if t < 9:
                    max_prob = max_tr_prob * self.emit_p[st][obs[t]][0][t]
                else:
                    max_prob = max_tr_prob * self.emit_p[st][obs[t]][0][9]
                
                #Set the overall probability of the tag and the state it came from
                V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

        for line in self.dptable(V):
            print(line)

        opt = []

        # Get the highest possible probable value for the final observed state
        max_prob = max(value["prob"] for value in V[-1].values())

        previous = None

        #Find that most probable final state
        for st, data in V[-1].items():
            if data["prob"] == max_prob:

                opt.append(st)

                previous = st

                break

        # Backtrack down and append
        for t in range(len(V) - 2, -1, -1):

            opt.append(V[t + 1][previous]["prev"])

            previous = V[t + 1][previous]["prev"]

        opt = list(reversed(opt))
        nopt = []
        for x in opt:
            nopt.append(x[0])
        nopt.append(opt[-1][1])

        return ''.join(nopt)

    def dptable(self, V):
        # Print a table of steps from dictionary
        yield " ".join(("%12d" % i) for i in range(len(V)))

        for state in V[0]:
            yield "%.7s: " % state + " ".join("%.7s" % ("%f" % v[state]["prob"]) for v in V)

    def learn(self, file = 'words.txt'):
        with open(file, 'r') as f:
            inp = f.readlines()
            for i in inp:
                wordList = list(i.strip().lower())
                for x in range(2,len(wordList)):
                    self.trans_p[wordList[x-2] + wordList[x-1]][1] += 1
                    for y in self.trans_p[wordList[x-2] + wordList[x-1]][0]:
                        self.trans_p[wordList[x-2] + wordList[x-1]][0][y] = ((self.trans_p[wordList[x-2] + wordList[x-1]][0][y]) * (len(self.states) + self.trans_p[wordList[x-2] + wordList[x-1]][1] - 1))/(len(self.states) + self.trans_p[wordList[x-2] + wordList[x-1]][1])
                    
                    self.trans_p[wordList[x-2] + wordList[x-1]][0][wordList[x-1] + wordList[x]] += 1/(self.trans_p[wordList[x-2] + wordList[x-1]][1] + len(self.states))

                nwords = []
                for i in range(1,len(wordList)):
                    nwords.append(wordList[i-1] + wordList[i])
                
                for x in nwords:
                    for i in self.emit_p[x]:
                        self.emit_p[x][i][1] += 1
                        if nwords.index(x) < 10:
                            self.emit_p[x][i][0][nwords.index(x)] = (self.emit_p[x][i][0][nwords.index(x)]*(self.emit_p[x][i][1] - 1))/self.emit_p[x][i][1]
                        else:
                            self.emit_p[x][i][0][9] = (self.emit_p[x][i][0][9]*(self.emit_p[x][i][1] - 1))/self.emit_p[x][i][1]

                    if nwords.index(x) < 10:
                        self.emit_p[x][x][0][nwords.index(x)] += 1/self.emit_p[x][i][1]
                    else:
                        self.emit_p[x][x][0][9] += 1/self.emit_p[x][i][1]


def createObj():
    hmm = autoCorrect()
    hmm.learn()
    pickle.dump(hmm, open("save.p", "wb"))
    return hmm

def getObj():
    hmm = pickle.load(open("save.p", "rb"))
    return hmm

def teachObj(file):
    hmm = pickle.load(open("save.p", "rb"))
    hmm.learn(file)
    pickle.dump(hmm, open("save.p", "wb"))
    return hmm

hmm = autoCorrect()
oldHmm = pickle.load(open("save.p", "rb"))
hmm.emit_p = oldHmm.emit_p
hmm.trans_p = oldHmm.trans_p
hmm.states = oldHmm.states
pickle.dump(hmm, open("save.p", "wb"))