# Tuple Warmup #1
# i
my_tup = ('diamond', 'club', 'spade', 'heart')
print(my_tup[::2])

# -> Suits for deck of cards.  These do not change so using tuple, an
#    immutable format, makes sense.

# ii
# ('diamond', 'spade')

# iii
print(my_tup[0])

# iv
print(my_tup[::2])

# v
# Indexing works the same as for lists

# vi
for item in my_tup:
    print(item)
# This functionality works just as it does for lists

# vii
# We CANNOT append 'gorilla' to the tuple, since tuples are immutable.
