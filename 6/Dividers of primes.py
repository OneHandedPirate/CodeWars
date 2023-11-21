# You are given a list of prime numbers (e.g. [5, 7, 11]) and a list of their
# associated powers (e.g. [2, 1, 1]). The product of those primes at their
# specified power forms a number x (in our case x = 5^2 * 7^1 * 11^1 = 1925).
#
# Your goal is to find all of the dividers for this number!
# To do so, you have to multiply each prime number, from its power 0 to its
# power p in the power list, to every other prime, from their power 0 to their
# associated power p.
#
# Each result of those products is a divider of x!
#
# In our example: [1, 5, 7, 11, 25, 35, 55, 77, 175, 275, 385, 1925]
#
# Once you find those dividers, sort them in ascending order, and VOILA!

from functools import reduce


def get_dividers(values: list[int], powers: list[int]) -> list[int]:
    prod = reduce(lambda x, y: x * y[0] ** y[1], zip(values, powers), 1)
    return sorted([num for num in range(1, prod + 1) if not prod % num])


assert get_dividers([5, 7, 11], [2, 1, 1]) == [1, 5, 7, 11, 25, 35, 55, 77, 175, 275, 385, 1925]
assert get_dividers([11, 113], [1, 1]) == [1, 11, 113, 1243]
assert get_dividers([2, 5, 13], [4, 3, 1]) == [1, 2, 4, 5, 8, 10, 13, 16, 20, 25, 26, 40, 50, 52, 65, 80, 100, 104, 125, 130, 200, 208, 250, 260, 325, 400, 500, 520, 650, 1000, 1040, 1300, 1625, 2000, 2600, 3250, 5200, 6500, 13000, 26000]