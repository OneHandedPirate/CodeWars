# Complete the function scramble(str1, str2) that returns true if a portion of
# str1 characters can be rearranged to match str2, otherwise returns false.
#
# Notes:
#
# Only lower case letters will be used (a-z). No punctuation or digits will be included.
# Performance needs to be considered.
# Examples
# scramble('rkqodlw', 'world') ==> True
# scramble('cedewaraaossoqqyt', 'codewars') ==> True
# scramble('katas', 'steak') ==> False


def scramble(s1: str, s2: str) -> bool:
    return all(c in s1 and s1.count(c) >= s2.count(c) for c in set(s2))


assert scramble('rkqodlw', 'world') is True
assert scramble('cedewaraaossoqqyt', 'codewars') is True
assert scramble('katas', 'steak') is False
assert scramble('aabbcamaomsccdd','commas') is True
