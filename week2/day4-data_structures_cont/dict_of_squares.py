nums_str_list = input('Please input numbers separated by dashes: ').split(' - ')

square_dict = {}
for num_str in nums_str_list:
    num = int(num_str)
    square_dict[num] = num ** 2

# Dict comp way of doing this
square_dict = {int(num): int(num) ** 2 for num in nums_str_list}

print(square_dict)
