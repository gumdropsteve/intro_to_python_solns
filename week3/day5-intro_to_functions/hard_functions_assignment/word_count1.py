def get_word_count(input_str):
    """Get the count of the number of words in the inputted string.

    We're assuming that words are separated by spaces, so we'll simply
    call the `.split()` method on the string and return the length of
    the resulting list.

    Args:
        input_str: String
    """

    words = input_str.split()
    word_count = len(words)
    return word_count

print(get_word_count("How many words is this?")) # Should be 5
print(get_word_count("This contains 4 words.")) # Should be 4
print(get_word_count("Let's try a really long string.")) # Should be 6
print(get_word_count("This is short.")) # Should be 3
print(get_word_count("One.")) # Should be 1
