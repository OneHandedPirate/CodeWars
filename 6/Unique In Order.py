# Implement the function unique_in_order which takes as argument a sequence and
# returns a list of items without any elements with the same value next to each
# other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1, 2, 2, 3, 3])   == [1, 2, 3]
# unique_in_order((1, 2, 2, 3, 3))   == [1, 2, 3]
from typing import Iterable


def unique_in_order(seq: Iterable):
    res = []
    cur = None
    for item in seq:
        if item != cur:
            res.append(item)
            cur = item
    return res if seq else []


assert unique_in_order("AA") == ["A"]
assert unique_in_order("AAAABBBCCDAABBB") == ["A", "B", "C", "D", "A", "B"]
assert unique_in_order("ABBCcA") == ["A", "B", "C", "c", "A"]
assert unique_in_order([1, 2, 3, 3, -1]) == [1, 2, 3, -1]
