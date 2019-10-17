# write a function that counts the number of times a given letter appears in a document
# the output should be in a dictionary 

def letter_counter(path_to_file, letters_to_count):
    # make a blank dictionary 
    dictionary = {}
    # add each letter to the dictionary 
    for letter in letters_to_count:
        # with it's current count (i.e. 0)
        dictionary.update({letter : 0})

    # open the file 
    with open(path_to_file) as f:
        # go through each line of the file
        for line in f:
            # go through each letter and it's count in the dictionary 
            for key in dictionary:
                # go through each character in the line 
                for char in line:
                    # if the character is the same as the key (letter we are looking for)
                    if char == key:
                        # update the count of that letter (key) in the dictionary 
                        dictionary[key] += 1

    # once that is all done, output the dictionary
    return dictionary


# if this file is called in terminal 
if __name__ == '__main__':
    # run letter_counter on data/test.txt and look for a, b, and c
    test = letter_counter('data/test.txt', 'abc')
    # then print the results
    print(test)
