# Dictionary Warmup #2
# i
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
for element in my_dct:
    print(element)
# > Texas
# > Indiana
# > Illinois
# > New York

# It prints the dictionary keys

# ii
# A dictionary is appropriate because these are key-value pairs (state-capitals)
#   where you only have unique state keys

# iii
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
for state in my_dct:
    print(state)

# iv
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
for state, capital in my_dct.items():
    print(state, capital)

# v
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
neighbor_dct = {}
neighbor_dct['Missouri'] = 'Jefferson City'
for state, capital in my_dct.items():
    print(state, capital)

# vi
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
neighbor_dct = {}
neighbor_dct['Missouri'] = 'Jefferson City'
my_dct.update(neighbor_dct)
for state, capital in my_dct.items():
    print(state, capital)

# vii
user_input = input("Input a state: \n")
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
try:
    print(user_input, my_dct[user_input])
except:
    print("Capital not found!")

# viii
user_input = input("Input a state: \n")
my_dct = {'Texas': 'Austin', 'Indiana': 'Indianapolis', 'Illinois': 'Chicago', \
          'New York': 'New York City'}
try:
    print(user_input, my_dct[user_input])
except:
    print("Capital not found!")
    new_dict = {}
    cap = input("Input the capital for this state: \n")
    new_dict[user_input] = cap
    my_dct.update(new_dict)
    print(my_dct)
