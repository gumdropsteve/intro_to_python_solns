def check_for_substring(lst_of_strings, substring):
    """Output a list of indices for those strings in lst_of_strings
    that contain the inputted substring.

    For each string in the lst_of_strings, see if the inputted substring
    is contained within that string. If it is, output its index, and if it's
    not, then don't.

    Args:
        lst_of_strings: List of Strings
        substring: String
    """

    output_lst = []
    for idx, string in enumerate(lst_of_strings):
        if substring in string:
            output_lst.append(idx)

    '''List comp. way
    output_lst = [idx for idx, string in enumerate(lst_of_strings)
                  if substring in string]
    '''

    return output_lst

print(check_for_substring(['This', 'is', 'an', 'example'], 'is'))
# Should return [0, 1]
print(check_for_substring(["Let's", 'try', 'another', 'example'], 'Le'))
# Should return [0]
print(check_for_substring(["Well", "input", 'a', 'really', 'long', 'string', 'here', 'with', 'a', 'bunch', 'of', 'words', ',', 'which', 'will', 'give', 'us', 'a', 'long', 'test'], 'll'))
# Should return [0, 3, 14]
print(check_for_substring(['Now', 'back', 'to', 'a', 'shorter', 'list', 'tack'], 'ack'))
# Should return [1, 6]
print(check_for_substring(['Test', 'for', 'nothing'], 'zada'))
# Should return []
