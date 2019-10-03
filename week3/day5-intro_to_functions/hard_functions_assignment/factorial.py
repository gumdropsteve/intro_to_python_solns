def calc_factorial(n):
    """Calculate the factorial of the inputted number.

    Args:
        n: Integer
    """

    factorial = 1
    for num in range(1, n + 1):
            factorial *= num

    return factorial

print(calc_factorial(5))  # 120
print(calc_factorial(3))  # 6
print(calc_factorial(2))  # 2
print(calc_factorial(6))  # 720
print(calc_factorial(1))  # 1
