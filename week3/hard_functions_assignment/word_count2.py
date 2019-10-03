def get_word_count(input_str, delimiter=' '):
    """Get the word count for the inputted string.

    Get the word count for the inputted string, where we consider
    words to be separated by the input delimiter (space by default).

    Args:
        input_str: String
        delimiter: String
    """

    words = input_str.split(delimiter)
    word_count = len(words)

    return word_count


print(get_word_count("separate,by,commas", ",")) # Should be 3.
print(get_word_count("Lets;try;using;semi;colons", ";")) # Should be 5.
print(get_word_count("What?about?using?question?marks", "?")) # Should be 5.
print(get_word_count("That was weird, let's go back to spaces.")) # Should be 8.
print(get_word_count("Check passing in a space now.", ' ')) # Should be 6. 
