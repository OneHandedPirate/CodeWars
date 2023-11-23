# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
#
# Finish the solution so that it returns the sum of all the multiples of 3 or 5
# below the number passed in.
#
# Additionally, if the number is negative, return 0.
#
# Note: If the number is a multiple of both 3 and 5, only count it once.


def solution(num: int) -> int:
    return sum(n for n in range(num) if not n % 3 or not n % 5)


assert solution(4) == 3
assert solution(6) == 8
assert solution(16) == 60
assert solution(3) == 0
