# There is an array with some numbers. All numbers are equal except for one.
# Try to find it!
#
# find_uniq([ 1, 1, 1, 2, 1, 1 ]) == 2
# find_uniq([ 0, 0, 0.55, 0, 0 ]) == 0.55
# It’s guaranteed that array contains at least 3 numbers.
#
# The tests contain some very huge arrays, so think about performance.


def find_uniq(arr: list[int | float]) -> int | float:
    x, y = set(arr)
    return x if arr.count(x) == 1 else y


assert find_uniq([1, 1, 1, 2, 1, 1]) == 2
assert find_uniq([0, 0, 0.55, 0, 0]) == 0.55
assert find_uniq([5, 5, 5, 5, 4, 5, 5, 5]) == 4
assert find_uniq([8, 8, 8, 8, 8, 8, 8, 7]) == 7
