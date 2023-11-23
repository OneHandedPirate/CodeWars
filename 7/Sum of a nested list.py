# Implement a function to calculate the sum of the numerical values
# in a nested list. For example :
#
# sum_nested([1, [2, [3, [4]]]]) -> 10


def sum_nested(lst):
    return sum(sum_nested(x) if hasattr(x, '__iter__') else x for x in lst)


assert sum_nested([1, [2, [3, [4]]]]) == 10
assert sum_nested([[[[], [], [[[[[[[[[[]]]]]]]]]]], [], [], [[[], [[]]]]], []]) == 0
assert sum_nested([1, [1], [1, [1]], [1, [1], [1, [1]]]]) == 8
assert sum_nested([[1, 2, 3, 4]]) == 10
assert sum_nested([[1], []]) == 1
