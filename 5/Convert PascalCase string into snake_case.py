# Complete the function/method so that it takes a PascalCase string and returns
# the string in snake_case notation. Lowercase characters can be numbers. If the
# method gets a number as input, it should return a string.
#
# Examples
# "TestController"  -->  "test_controller"
# "MoviesAndBooks"  -->  "movies_and_books"
# "App7Test"        -->  "app7_test"
# 1                 -->  "1"


def to_underscore(string: str) -> str:
    return ''.join('_'+c.lower() if c.isupper() else c for c in str(string)).lstrip('_')


assert to_underscore("TestController") == "test_controller"
assert to_underscore("MoviesAndBooks") == "movies_and_books"
assert to_underscore("App7Test") == "app7_test"
