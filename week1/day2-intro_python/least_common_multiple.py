user_str1 = ''
while not user_str1.isdigit():
    user_str1 = input('Please input a number: ')
user_inputted_num1 = int(user_str1)

user_str2 = ''
while not user_str2.isdigit():
    user_str2 = input('Please input another number: ')
user_inputted_num2 = int(user_str2)

print('The least common multiple of these two numbers is: ')

idx = user_inputted_num1
if idx > user_inputted_num2:
    idx = user_inputted_num2

while True:
    if  idx % user_inputted_num1 == 0 and idx % user_inputted_num2 == 0:
        #found = True
        print(idx)
        break
    idx += 1
