user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a series element to compute: ')
series_element = int(user_str)

print('The element of the series you are looking for is: ')
a = 1 # The start of the series.

idx = 0

while idx < series_element:
    a = a * 2 + 1
    idx += 1

print(a)
