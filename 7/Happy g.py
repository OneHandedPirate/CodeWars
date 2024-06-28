# Let's say that "g" is happy in the given string, if there is another
# "g" immediately to the right or to the left of it.
#
# Find out if all "g"s in the given string are happy.
#
# Example
# For str = "gg0gg3gg0gg", the output should be true.
#
# For str = "gog", the output should be false.
#
# Input/Output
# [input] string str
# A random string of lower case letters, numbers and spaces.
#
# [output] a boolean value
# true if all "g"s are happy, false otherwise.


def happy_g(st: str) -> bool:
    sequence = 0
    for letter in st:
        if letter == 'g':
            sequence += 1
        else:
            if sequence == 1:
                return False
            sequence = 0
    return True


assert happy_g("gg0gg3gg0gg") is True
assert happy_g("gog") is False
assert happy_g("bigger is ggooder") is True
