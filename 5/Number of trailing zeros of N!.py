# Write a program that will calculate the number of trailing zeros in a
# factorial of a given number.
#
# N! = 1 * 2 * 3 *  ... * N
#
# Be careful 1000! has 2568 digits...
#
# For more info, see: http://mathworld.wolfram.com/Factorial.html
#
# Examples
# N	Product	N factorial	Trailing zeros
# 6	1*2*3*4*5*6	720	1
# 12	1*2*3*4*5*6*7*8*9*10*11*12	479001600	2
# Hint: You're not meant to calculate the factorial. Find another way to find
# the number of zeros.


def zeroes(n: int) -> int:
    z = 0
    while n >= 5:
        n //= 5
        z += n
    return z


assert zeroes(6) == 1
assert zeroes(12) == 2
assert zeroes(1000000000) == 249999998


