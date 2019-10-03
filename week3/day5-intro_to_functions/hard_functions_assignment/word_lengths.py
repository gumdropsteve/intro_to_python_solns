def get_word_lengths(input_str, delimiter=' '):
    """Get the lengths of each word in the inputted string.

    Get the lengths of each wordin the inputted string, where we consider
    words to be separated by the input delimiter (space by default).

    Args:
        input_str: String
        delimiter: String
    """

    words = input_str.split(delimiter)
    word_lengths = [len(word) for word in words]

    return word_lengths


print(get_word_lengths("separate,by,commas", ","))
# Should be [8, 2, 6]
print(get_word_lengths("Lets;try;using;semi;colons", ";"))
# Should be [4, 3, 5, 4, 6]
print(get_word_lengths("What?about?using?question?marks", "?"))
# Should be [4, 5, 5, 8, 5]
print(get_word_lengths("That was weird, let's go back to spaces."))
# Should be [4, 3, 6, 5, 2, 4, 2, 7]
print(get_word_lengths("Check passing in a space now.", ' '))
# Should be [5, 7, 2, 1, 5, 4]
