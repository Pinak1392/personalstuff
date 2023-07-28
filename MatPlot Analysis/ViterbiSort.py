from timeit import default_timer as timer
from Matplot import plot
import random
from Viterbi_Algorithm import viterbi, BruteForce
from math import exp

#HMM

#Hidden States
states = ['C', 'D', 'E']

#The Probability of going from hidden state to next hidden state
trans_p = {
   'C' : {'D': 0.3, 'C': 0.4, 'E': 0.3},
   'D' : {'C': 0.2, 'D': 0.3, 'E': 0.5},
   'E' : {'C': 0, 'D': 0.8, 'E': 0.2}
}

initial = {'C': 0.0, 'D': 1.0, 'E': 0.0}

#The probability of a certain state being a certain observable state
emit_p = {
   'C' : {'A': 0.5, 'B': 0.5},
   'D' : {'A': 0.1, 'B': 0.9},
   'E' : {'A': 0.4, 'B': 0.6}
}

# input sizes
input_sizes = [x for x in range(4,51,1)]

# average_times will be stored for each input_size
average_times1 = []

# run trial on each input size
for size in input_sizes:
    # record the times taken for each input size
    times = []
    emit_p[str(size)] = {'A': 0, 'B': 0}
    states.append(str(size))
    for i in trans_p:
        trans_p[i][str(size)] = 0
    trans_p[str(size)] = trans_p['C']
    initial[str(size)] = 0

    # perform 20 trials
    for trial_number in range(20):

        # construct a set of input data
        my_data = ['A','B','B']

        #print("input:", my_data)   # uncomment this line to output the original list

        # begin timer
        start = timer()

        viterbi(my_data,states,initial,trans_p,emit_p)

        # end timer
        end = timer()

        # calculate running time (measured in seconds)
        running_time = end - start

        # add it to our list of times
        times.append(running_time)
    # print(running_time)

    # sorted_data is now the sorted version of the original list
    # print("result", sorted_data)  # uncomment this line to see the sorted version

    # calculate the average time and append to our list of average_times
    average_times1.append(sum(times) / float(len(times)))  # float just in case python 2 is used
    print(size)


#HMM

#Hidden States
states = ['C', 'D', 'E']

#The Probability of going from hidden state to next hidden state
trans_p = {
   'C' : {'D': 0.3, 'C': 0.4, 'E': 0.3},
   'D' : {'C': 0.2, 'D': 0.3, 'E': 0.5},
   'E' : {'C': 0, 'D': 0.8, 'E': 0.2}
}

initial = {'C': 0.0, 'D': 1.0, 'E': 0.0}

#The probability of a certain state being a certain observable state
emit_p = {
   'C' : {'A': 0.5, 'B': 0.5},
   'D' : {'A': 0.1, 'B': 0.9},
   'E' : {'A': 0.4, 'B': 0.6}
}

# average_times will be stored for each input_size
average_times2 = []

# run trial on each input size
for size in input_sizes:

    # record the times taken for each input size
    times = []
    emit_p[str(size)] = {'A': 0, 'B': 0}
    states.append(str(size))
    for i in trans_p:
        trans_p[i][str(size)] = 0
    trans_p[str(size)] = trans_p['C']
    initial[str(size)] = 0

    # perform 20 trials
    for trial_number in range(20):

        # construct a set of input data
        my_data = ['A','B','B']

        #print("input:", my_data)   # uncomment this line to output the original list

        # begin timer
        start = timer()

        BruteForce(my_data,states,initial,trans_p,emit_p)

        # end timer
        end = timer()

        # calculate running time (measured in seconds)
        running_time = end - start

        # add it to our list of times
        times.append(running_time)
    # print(running_time)

    # sorted_data is now the sorted version of the original list
    # print("result", sorted_data)  # uncomment this line to see the sorted version

    # calculate the average time and append to our list of average_times
    average_times2.append(sum(times) / float(len(times)))  # float just in case python 2 is used
    print(size)

time3 = [exp(x)/50000 for x in input_sizes]

plot('Hidden states increase comparison', 'states', 'time', input_sizes, [[average_times1,'r','Viterbi Algorithm'], [average_times2,'b','Brute Force Algorithm']])