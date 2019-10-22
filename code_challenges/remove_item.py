# Write a function that removes one occurrence of a given item from a list. 
# Do not use methods .pop() or.remove()! 
# If the item is not present in the list, the output should be ‘The item is not in the list’


def remove_item(list_items, item_to_remove):
    """
    Remove first occurence of item from list
    """
    # make a new list (start with it blank)
    new_list = []
    # track how many times the item was found
    item_found_count = 0

    # go through each item
    for item in list_items:
        # if the item is not the item we are looking for
        if item != item_to_remove:
            # add that item to the new list
            new_list.append(item)
        # the item is the item we are looking for
        else:
            # update the number of times we've found the item
            item_found_count += 1
            # if we have found the item more than once
            if item_found_count > 1:
                # add this instance of the item to the new list 
                # we only want to remove the first instance of the item
                new_list.append(item)
    
    # if the item was found
    if item_found_count > 0:
        # output the new list
        return new_list
    # otherwise (if the item was not found)
    else:
        # return the given error message
        return 'The item is not in the list'
            
        

if __name__ == '__main__':
    # define a test list 
    test_items_list = ['cat', 4, 'dog', 2, 'cat', '0', 'human']
    # define a test target
    test_item_to_remove = 'cat'
    # run the test
    test = remove_item(test_items_list, test_item_to_remove)
    # display the outcome -- [4, 'dog', 2, 'cat', '0', 'human']
    print(test)
