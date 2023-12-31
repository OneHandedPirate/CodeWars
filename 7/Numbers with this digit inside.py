# You have to search all numbers from inclusive 1 to inclusive a given number x,
# that have the given digit d in it.
# The value of d will always be 0 - 9.
# The value of x will always be greater than 0.
#
# You have to return as an array
#
# the count of these numbers,
# their sum
# and their product.
#
# For example:
# x = 11
# d = 1
# ->
# Numbers: 1, 10, 11
# Return: [3, 22, 110]
#
# If there are no numbers, which include the digit, return [0,0,0].
from functools import reduce


def numbers_with_digit_inside(x: int, d: int) -> list[int, int, int]:
    d = str(d)
    res = [num for num in range(1, x + 1) if d in str(num)]
    return [len(res), sum(res), reduce(lambda x, y: x * y, res) if res else 0]


assert numbers_with_digit_inside(11, 1) == [3, 22, 110]
assert numbers_with_digit_inside(7, 6) == [1, 6, 6]
assert numbers_with_digit_inside(20, 0) == [2, 30, 200]
assert numbers_with_digit_inside(44, 4) == [9, 286, 5955146588160]

