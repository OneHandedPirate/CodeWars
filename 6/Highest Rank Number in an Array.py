# Complete the method which returns the number which is most frequent in the
# given input array. If there is a tie for most frequent number,
# return the largest number among them.
#
# Note: no empty arrays will be given.
#
# Examples
# [12, 10, 8, 12, 7, 6, 4, 10, 12]              -->  12
# [12, 10, 8, 12, 7, 6, 4, 10, 12, 10]          -->  12
# [12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]  -->   3

from collections import Counter


def highest_rank(arr: list) -> int:
    counter = Counter(arr)
    return max(y[0] for y in filter(lambda x: x[1] == max(counter.values()), counter.items()))


assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12]) == 12
assert highest_rank([12, 10, 8, 12, 7, 6, 4, 10, 12, 10]) == 12
assert highest_rank([12, 10, 8, 8, 3, 3, 3, 3, 2, 4, 10, 12, 10]) == 3
