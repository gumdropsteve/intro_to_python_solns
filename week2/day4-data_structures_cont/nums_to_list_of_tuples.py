num_string = input('Please input numbers separated by commas: ')

nums = num_string.split(', ')

tuple_list = []
for two in zip(nums[::2], nums[1::2]):
    tuple_list.append(two)

# List comp way of doing this
tuple_list = [two for two in zip(nums[::2], nums[1::2])]

print(tuple_list)
