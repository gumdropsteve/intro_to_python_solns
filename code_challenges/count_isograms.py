# implement a function that counts the number of isograms in a list of words (strings)
# an isogram is a word that has no repeating letters, consecutive or nonconsecutive

def count_isograms(list_of_words):
    # initiate a count
    isogram_count = 0

    # go through each word in the list
    for word in list_of_words:

        # make a note of how long a word is
        word_length = len(word)
        # start a count of how many unique letters are in that word
        unique_letters_in_word = 0

        # go through each letter in that word
        for letter in word:
            # if the letter occours just once
            if word.count(letter) == 1:
                # add 1 to the number of unique letters in the word
                unique_letters_in_word += 1

        # if all letters in the word are unique
        if word_length == unique_letters_in_word:
            # add 1 to the count of isograms
            isogram_count += 1

    # output the final count
    return isogram_count


# if this file is called in terminal
if __name__ == '__main__':
    # make a base case 
    base_case = ['conduct', 'letter', 'contract', 'hours', 'interview']
    # run isogram count on the base case
    test = count_isograms(base_case)
    # display the outcome
    print(test)
