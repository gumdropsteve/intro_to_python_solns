def check_divisor(input_lst, n):
    """Ouput 'yes' or 'no' if the element in the input_lst is divisible by n.

    Check if each element in the input_lst is divisible by n, and output a
    list of 'yes' or 'no' depending on whether or not they are divisible.

    Args:
        input_lst: List of Integers
        n: Integer
    """

    output_lst = []
    for element in input_lst:
        if not element % n:
            output_lst.append('yes')
        else:
            output_lst.append('no')

    ''' List comprehension way to do this.

    output_lst = ['yes' if not element % n else 'no' for element in input_lst]

    '''

    return output_lst

print(check_divisor([1, 2, 3, 4, 5], 3)) # ['no', 'no', 'yes', 'no', 'no']
print(check_divisor([2, 4, 6, 8, 10], 2)) # ['yes', 'yes', 'yes', 'yes', 'yes']
print(check_divisor([2, 3, 7, 12, 16], 4)) # ['no', 'no', 'no', 'yes', 'yes']
print(check_divisor([3, 6, 7, 25, 63], 3)) # ['yes', 'yes', 'no', 'no', 'yes']
print(check_divisor([5, 16, 23, 42, 50], 5)) # ['yes', 'no', 'no', 'no', 'yes']
