#Hidden Markov Model Courtesy of wikipedia viterbi algorithm

#The Observable States
obs = ['A', 'B', 'A', 'B', 'A', 'B', 'A', 'A']

#Hidden States
states = ('C', 'D', 'E')

#The Probability of going from hidden state to next hidden state
trans_p = {
   'C' : {'D': 0.4, 'C': 0.3, 'E': 0.3},
   'D' : {'C': 0.3, 'D': 0.3, 'E': 0.4},
   'E' : {'C': 0.4, 'D': 0.3, 'E': 0.3}
}

initial = {'C': 0.4, 'D': 0.3, 'E': 0.3}

#The probability of a certain state being a certain observable state
emit_p = {
   'C' : {'A': 0.5, 'B': 0.5},
   'D' : {'A': 0.1, 'B': 0.9},
   'E' : {'A': 0.4, 'B': 0.6}
}


#Viterbi Algorithm taken from wikipedia for viterbi algortithm
def viterbi(obs, states, start_p, trans_p, emit_p):

    V = [{}]

    if len(obs) == 0:
        return []

    #Sets up the initial probabilities based on the first observed state
    for st in states:
        #Finds the overall initial probability by multiplying the probability of event given state by the probability of the state initially
        V[0][st] = {"prob": start_p[st] * emit_p[st][obs[0]], "prev": None}

    # Run when length of observed is greater than 1
    for t in range(1, len(obs)):

        #Create a new set of probabilities for the next observation
        V.append({})

        for st in states:
            #Find the starting maximum probability from the probability of a starting tag given previous tag probability and transition probability
            max_tr_prob = V[t-1][states[0]]["prob"]*trans_p[states[0]][st]

            #Stores the selected most probable state 
            prev_st_selected = states[0]

            for prev_st in states[1:]:
                #Gets the probability of a state given a previous state chance of transition and its probability
                tr_prob = V[t-1][prev_st]["prob"]*trans_p[prev_st][st]

                #If the found probability is greater than the max probability, change it to the new one
                if tr_prob > max_tr_prob:

                    max_tr_prob = tr_prob

                    #Also change the probable previous state to the one transitioned from by the new probability
                    prev_st_selected = prev_st

                    
            #Get overall max probability of tag from maximum transition probability and the probability that it emitted the observed state
            max_prob = max_tr_prob * emit_p[st][obs[t]]
            
            #Set the overall probability of the tag and the state it came from
            V[t][st] = {"prob": max_prob, "prev": prev_st_selected}

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

    opt = ' '.join(reversed(opt))
    return f'The steps of states are {opt} with highest probability of {max_prob}'