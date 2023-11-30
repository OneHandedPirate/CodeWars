# Complete the solution so that it splits the string into pairs of two characters.
# If the string contains an odd number of characters then it should replace the
# missing second character of the final pair with an underscore ('_').
#
# Examples:
#
# * 'abc' =>  ['ab', 'c_']
# * 'abcdef' => ['ab', 'cd', 'ef']


def solution(s: str) -> list[str]:
    return [s[i:i+2].ljust(2, '_') for i in range(0, len(s), 2)]


assert solution("asdfadsf") == ['as', 'df', 'ad', 'sf']
assert solution("asdfads") == ['as', 'df', 'ad', 's_']
assert solution("") == []
assert solution("x") == ["x_"]
