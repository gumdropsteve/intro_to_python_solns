# Set Warmup #3
# i
my_set = {2, 3, 5}
for num in my_set:
    print(num)
# This works the same as for lists

# ii
my_set = {2, 3, 5}
my_fav_primes = {13, 3, 19}
for num in my_set:
    print(num)

# iii
my_set = {2, 3, 5}
my_fav_primes = {13, 3, 19}
common = my_set.intersection(my_fav_primes)
for num in common:
    print(num)

# iv
my_set = {2, 3, 5}
my_fav_primes = {13, 3, 19}
diff = my_set.symmetric_difference(my_fav_primes)
for num in diff:
    print(num)

# v
my_set = {2, 3, 5}
my_fav_primes = {13, 3, 19}
my_tot_primes = my_set.union(my_fav_primes)
for num in my_tot_primes:
    print(num)

# vi
user_prime = int(input("Enter a prime number to add to the set: \n"))
user_prime_set = []
user_prime_set.append(user_prime)
user_prime_set = set(user_prime_set)
my_set = {2, 3, 5}
my_fav_primes = {13, 3, 19}
my_tot_primes = my_set.union(my_fav_primes)
my_tot_primes = my_tot_primes.union(user_prime_set)
for num in my_tot_primes:
    print(num)
