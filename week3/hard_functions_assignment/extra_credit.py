def calculate_taxes(tax_tup_lst, income):
    """Calculate taxes for a given income.

    The tax tuple list contains tuples with two values, the first of
    which is an income upper bound and the second of which is a tax rate
    for all income up to the given income bound. If any income is left
    passed the highest income bound given, it is taxed at the rate for
    that highest income bound. For example if the tax_tup_lst is:

    [(50000, 0.08), (100000, 0.10), (150000, 0.15)]

    Then the first 50k is taxed at 8%, the second 50k at 10%, and
    the rest of your income at 15%. This function will calculate the total
    taxes for an inputted income.

    Args:
        tax_tup_lst: List of tuples
        income: Integer
    """

    # This will make sure that we iterate through the tax ranges
    # in order, as we should.
    tax_tup_lst = sorted(tax_tup_lst, key=lambda x: x[0])

    tot_taxes = 0
    for tax_max, tax_rate in tax_tup_lst:
        last_tax_rate = tax_rate
        if income <= tax_max:
            tot_taxes += income * tax_rate
            income = max(income - tax_max, 0)
            break
        else:
            tot_taxes += tax_max * tax_rate
            income = income - tax_max

    # Now to account for any income left over.
    tot_taxes = tot_taxes if income < 0 else tot_taxes + (income * last_tax_rate)

    return tot_taxes

print('Round 1 - Sorted Examples')
print('-' * 50)
print(calculate_taxes([(50000, 0.08), (100000, 0.10), (150000, 0.15)], 70000))
# Should return 6000
print(calculate_taxes([(50000, 0.08), (100000, 0.10), (150000, 0.15), (200000, 0.20)], 70000))
# Should return 6000
print(calculate_taxes([(10000, 0.02), (20000, 0.08)], 30000))
# Should return 1800
print(calculate_taxes([(50000, 0.08)], 70000))
# Should return 5600
print(calculate_taxes([(10000, 0.04), (20000, 0.06), (30000, 0.08), (40000, 0.10), (50000, 0.20)], 30000))
# Should return 1600

print
print('Round 2 - Unsorted Examples')
print('-' * 50)
# Now to test for unsorted stuff. Let's just do this by rearranging the order
# of stuff from earlier.
print(calculate_taxes([(100000, 0.10), (150000, 0.15), (50000, 0.08)], 70000))
# Should return 6000
print(calculate_taxes([(200000, 0.20), (100000, 0.10), (50000, 0.08), (150000, 0.15)], 70000))
# Should return 6000
print(calculate_taxes([(20000, 0.08), (10000, 0.02)], 30000))
# Should return 1800
print(calculate_taxes([(50000, 0.08)], 70000))
# Should return 5600
print(calculate_taxes([(30000, 0.08), (20000, 0.06), (40000, 0.10), (10000, 0.04)], 30000))
# Should return 1600
