first_nums_string = input('Please enter a list of comma separated numbers: ')
second_nums_string = input('Please enter another list of comma separated numbers: ')

first_nums_set = set(first_nums_string.split(', '))
second_nums_set = set(second_nums_string.split(', '))

common_nums = first_nums_set & second_nums_set

print(', '.join(common_nums))
