# write a function that counts the number of times a given letter appears in a document
# the output should be in a dictionary 

def letter_counter(path_to_file, letters_to_count):
    # create an empty dictionary
    dictionary = {}
    # go through each letter to count
    for letter in letters_to_count:
        # add each to dictionary 
        dictionary.update({letter : 0})
    # go through each letter in the dictionary
    for key in dictionary:
        # open the file 
        with open(path_to_file) as new_file:
            # examine each line
            for line in new_file:
                # go through each letter in that line
                for letter in line:
                    # check if the key is the same as the letter
                    if letter == key:
                        # increase the value for that key by 1
                        dictionary[key] += 1
    # output the results
    return dictionary


if __name__=='__main__':
    # run a test
    test = letter_counter('data/test.txt', 'abcd')
    print(test)
