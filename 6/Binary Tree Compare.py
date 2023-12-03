# Given the node object:
#
# Node:
#   val: <int>,
#   left: <Node> or null,
#   right: <Node> or null
# write a function compare(a, b) which compares the two trees defined by Nodes
# a and b and returns true if they are equal in structure and in value and false otherwise.
#
# Examples:
#
# 1       1
# | \     | \
# 2  3    2  3
# => true
#
# 1       1
# | \     | \
# 3  3    2  3
# => false (values not the same 2 != 3)
#
# 1       1
# | \     |
# 2  3    2
#         |
#         3
# => false (structure not the same)


def compare(a, b):
    if a is None or b is None:
        return a is b
    return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right)

# def compare(a, b):
#     return a.val == b.val and compare(a.left, b.left) and compare(a.right, b.right) if a and b else a is b