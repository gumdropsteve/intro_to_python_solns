user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a number to compute the factorial of: ')
user_inputted_num = int(user_str)

idx = user_inputted_num
factorial = 1

while idx > 0:
    factorial *= idx
    idx -= 1

print(factorial)
