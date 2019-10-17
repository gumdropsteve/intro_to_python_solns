# write a function that manually sorts a list of integers
# do not use the built-in sorted() function or the .sort() string method
# write out your entire algorithm (hint: there are lots of ways to accomplish this task)

def manual_sort(data_list):
    # make a copy of the unordered list
    unsorted_list = data_list.copy()
    # make a blank list for ordered 
    sorted_list = []
    
    # starting with the 0th index
    i = 0
    # assume the 0th value in the unordered list is the lowest
    lowest = unsorted_list[0]

    # as long as there are still numbers in the unordered list
    while len(unsorted_list) > 0:
        # if the number at index i is less than current assumed lowest value
        if  unsorted_list[i] < lowest:
            # set that number to the new lowest value
            lowest = unsorted_list[i]

        # increase the index by 1
        i += 1

        # if the index range of the unordered list has been exausted (i.e. we've gone through all numbers)
        if i == len(unsorted_list):
            # then we have found the current lowest value in the unordered list
            # so add it to the sorted list
            sorted_list.append(lowest)
            # then remove it from the unordered list
            unsorted_list.remove(lowest)
            # if the unordered list still exists (i.e. it still has numbers in it)
            if unsorted_list:
                # go back to assuming the 1st number (at index 0) is the smallest number
                lowest = unsorted_list[0]
            # and reset the index (i) so we can start the process over
            i = 0

    # once all values from the unordered list have been added to the ordered list
    # output the final (sorted) list
    return sorted_list


# if this file is called by python
if __name__ == '__main__':
    # make a base case (i.e. a test case)
    base_case = [4, 2, 0, 6, 9]
    # run the manual_sort function of the base case
    test = manual_sort(base_case)
    # share the outcome in terminal
    print(test)
    