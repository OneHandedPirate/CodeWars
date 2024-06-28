# As part of this kata, you need to find the length of the sub-array that begins
# and ends with the specified number.
#
# For example, if the array arr is [0, -3, 7, 4, 0, 3, 7, 9], finding the length
# of the sub-array that begins and ends with 7s would return 5.
#
# For sake of simplicity, there will only be numbers (positive or negative) in
# the supplied array.
#
# If there are less or more than two occurrences of the number to search for,
# return 0.

def length_of_sequence(arr: list[int], n: int) -> int:
    if arr.count(n) != 2:
        return 0
    a = arr.index(n)
    b = arr.index(n, a + 1)
    return b - a + 1


assert length_of_sequence([0, -3, 7, 4, 0, 3, 7, 9], 7) == 5
assert length_of_sequence([0, 8, -7, 6, 1, 2, -7, 4, 8, 9], 8) == 8
assert length_of_sequence([-7, 5, 0, 2, 9, 5], 5) == 5
