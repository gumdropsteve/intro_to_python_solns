user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a number to compute the factorial of: ')
user_inputted_num = int(user_str)

factorial = 1
for num in range(1, user_inputted_num + 1):
    factorial *= num

print(factorial)
