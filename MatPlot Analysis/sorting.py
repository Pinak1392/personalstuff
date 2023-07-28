# timed selection sort implementation

# import required modules
import random
from timeit import default_timer as timer
from Matplot import plot
from BinarySearch import mergeBinSearch, selectBinSearch, pysortBinSearch
from LinearSearch import linSearch
from math import log

def sortTime(msize, f):
    # input sizes
    input_sizes = [x for x in range(0,msize, 100)]

    # average_times will be stored for each input_size
    average_times = []

    # run trial on each input size
    for size in input_sizes:

        # record the times taken for each input size
        times = []

        # perform 20 trials
        for trial_number in range(20):

            # construct a random set of input data
            my_data = []
            for i in range(size + 1):
                my_data.append(random.randint(-100,100))

            #print("input:", my_data)   # uncomment this line to output the original list

            # begin timer
            start = timer()

            f(my_data)

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
        average_times.append(sum(times) / float(len(times)))  # float just in case python 2 is used
        print(size + 1)

    return average_times

# print average "running times" for each input size
#for i in range(len(input_sizes)):
# print("Running time for input size",input_sizes[i], "is", average_times[i])

input_sizes = 10000
average_times = sortTime(input_sizes, linSearch)
average_times2 = sortTime(input_sizes, selectBinSearch)
average_times3 = sortTime(input_sizes, mergeBinSearch)
average_times4 = sortTime(input_sizes, pysortBinSearch)

xvals = [x + 1 for x in range(0,input_sizes,100)]

plot(xvals,[[average_times,'r','linSearch'],[average_times2,'b','selectBinSearch'],[average_times3,'g','mergeBinSearch'],[average_times4,'m','pysortBinSearch']])
