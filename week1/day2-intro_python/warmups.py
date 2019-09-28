# Day 2
# Warmup # 1
a = int(input("Input a positive integer: "))
b = int(input("Input another positive integer: "))

ab_sum = 0
i = 0
while i < b:
    ab_sum += a
    i += 1
print(f"The product of {a} * {b}) = {ab_sum}")


# Warmup #2
a = int(input("Input a positive integer: "))
b = int(input("Input another positive integer: "))

ab_diff = a
i = 0
while ab_diff >= b:
    ab_diff -= b
    i += 1
print(f"{a} / {b}) = {i}")

# Warmup #3
a = int(input("Input a positive integer: "))
b = int(input("Input another positive integer: "))

ab_mult = 1
i = 0
while i < b:
    ab_mult *= a
    i += 1
print(f"{a} ** {b}) = {ab_mult}")

# Warmup #4
a = int(input("Input a positive integer: "))
b = int(input("Input another positive integer: "))

if (a % b == 0):
    print(f"{b} divides evenly into {a}.")
else:
    print(f"{b} does not divide evenly into {a}.")


# Warmup #5
from random import randint

answer = randint(1,100)
print("Welcome to the Number Guessing Game!")
guess = int(input("Please input your first guess (1-100): "))

if guess == answer:
    print("You are right!  Congratulations!")
else:
    while guess != answer:
        if guess < answer:
            print("Your guess was too low.")
        else:
            print("Your guess was too high.")
        guess = int(input("Please try again: "))
    print("You are right!  Congratulations!")
