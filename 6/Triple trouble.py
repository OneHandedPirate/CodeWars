# Write a function
#
# triple_double(num1, num2)
# which takes numbers num1 and num2 and returns 1 if there is a straight
# triple of a number at any place in num1 and also a straight double of the same number in num2.
#
# If this isn't the case, return 0
#
# Examples
# triple_double(451999277, 41177722899) == 1
# # num1 has straight triple 999s and num2 has straight double 99s
#
# triple_double(1222345, 12345) == 0
# # num1 has straight triple 2s but num2 has only a single 2
#
# triple_double(12345, 12345) == 0
#
# triple_double(666789, 12345667) == 1


def triple_double(num1: int, num2: int) -> int:
    num1_str = str(num1)
    triples = []
    for i in range(len(num1_str) - 2):
        if num1_str[i] == num1_str[i+1] == num1_str[i+2]:
            triples.append(num1_str[i])
    if not triples:
        return 0

    num2_str = str(num2)
    for i in range(len(num2_str) - 1):
        if num2_str[i] == num2_str[i+1] and num2_str[i] in triples:
            return 1
    return 0


def triple_double(num1: int, num2: int) -> int:
    for x in range(10):
        if str(num1).count(str(x)*3) and str(num2).count(str(x)*2):
            return 1
    return 0


def triple_double(num1: int, num2: int) -> int:
    return any(i * 3 in str(num1) and i * 2 in str(num2) for i in '0123456789')


assert triple_double(451999277, 41177722899) == 1
assert triple_double(1222345, 12345) == 0
assert triple_double(12345, 12345) == 0