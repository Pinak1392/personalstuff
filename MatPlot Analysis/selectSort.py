def selectSort(my_data):
    # perform sort
    # find lowest value in list - continue while we still have values
    sorted_data = []
    while len(my_data) > 0:
        # each time through reset the lowest value
        lowest = None

        # step through list, looking for lowest value
        for item in my_data:
            if lowest == None or lowest > item:
                lowest = item

        # append the lowest value to the sorted list
        sorted_data.append(lowest)

        # remove the value from the original list
        my_data.remove(lowest)

    return sorted_data