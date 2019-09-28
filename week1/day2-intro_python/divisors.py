user_str = ''
while not user_str.isdigit():
    user_str = input('Please input a number to get the divisors of: ')
user_inputted_num = int(user_str)

print('Our divisors are: ')

idx = user_inputted_num

while idx > 0:
    if user_inputted_num % idx == 0:
        print(idx)
    idx -= 1
