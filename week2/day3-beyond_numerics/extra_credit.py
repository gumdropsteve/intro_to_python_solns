lst1, lst2 = [], []
while len(lst1) < 8:
    user_num = int(input('Please enter a number for list 1: '))
    lst1.append(user_num)

while len(lst2) < 8:
    user_num = int(input('Please enter a number for list 2: '))
    lst2.append(user_num)

# Way to do this with a for loop.
common_elements = []
for element in lst1:
    if element in lst2:
        common_elements.append(element)

# Using a list comp for this.
common_elements = [element for element in lst1 if element in lst2]

common_elements.sort()
print(common_elements)
