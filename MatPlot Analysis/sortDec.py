from recursion import make_digit_string, val_to_dec
from timeit import default_timer as timer
from Matplot import plot

# input sizes
input_sizes = [x for x in range(1,50, 1)]

# average_times will be stored for each input_size
average_times1 = []
average_times2 = []

# run trial on each input size
for size in input_sizes:
    # record the times taken for each input size
    times = []
    times2 = []

    # perform 20 trials
    for trial_number in range(20):
        # begin timer
        start = timer()

        a = make_digit_string(2, size)

        # end timer
        end = timer()

        # calculate running time (measured in seconds)
        running_time = end - start

        # add it to our list of times
        times.append(running_time)

        # begin timer
        start = timer()

        val_to_dec(size, a[0])

        # end timer
        end = timer()

        # calculate running time (measured in seconds)
        running_time = end - start

        # add it to our list of times
        times2.append(running_time)
    # print(running_time)

    # sorted_data is now the sorted version of the original list
    # print("result", sorted_data)  # uncomment this line to see the sorted version

    # calculate the average time and append to our list of average_times
    average_times1.append(sum(times) / float(len(times)))
    average_times2.append(sum(times2) / float(len(times2)))  # float just in case python 2 is used
    print(size + 1)

xvals = [x + 1 for x in range(1,50,1)]

plot(xvals,[[average_times1,'r','createStr'], [average_times2,'b','decodeStr']])