def filter_by_end_letter(string_lst, check_letter):
    """Filter the string list to those words that end with the check_letter.

    Args:
        string_lst: List of strings
        check_letter: String (one letter)
    """

    output_lst = []
    for string in string_lst:
        if string.endswith(check_letter):
            output_lst.append(string)

    '''List comp. way

    output_lst = [string for string in string_lst
                  if string.endswith(check_letter)]
    '''

    return output_lst

print(filter_by_end_letter(['I', 'am', 'in', 'love', 'with', 'python'], 'n'))
# Should return ['in', 'python']
print(filter_by_end_letter(['Python', 'is', 'amazing'], 'g'))
# Should return ['amazing']
print(filter_by_end_letter(['This', 'is', 'a', 'silly', 'question'], 's'))
# Should return ['This', 'is']
print(filter_by_end_letter(['Hello', 'goodbye'], 'g'))
# Should return []
print(filter_by_end_letter(['Statistics', 'is' , 'kind', 'of', 'fun', 'sometimes'], 's'))
# Should return ['Statistics', 'is', 'sometimes']
