# ...Or rather, what's a name in? For us, a particular string is where we are
# looking for a name.
#
# Task
# Write a function, taking two strings in parameter, that tests whether or not
# the first string contains all of the letters of the second string, in order.
#
# The function should return true if that is the case, and else false. Letter
# comparison should be case-INsensitive.
#
# Examples
#     "Across the rivers", "chris" --> true
#       ^      ^  ^^   ^
#       c      h  ri   s
#
#     Contains all of the letters in "chris", in order.
# ----------------------------------------------------------
#     "Next to a lake", "chris" --> false
#
#     Contains none of the letters in "chris".
# --------------------------------------------------------------------
#     "Under a sea", "chris" --> false
#          ^   ^
#          r   s
#
#     Contains only some of the letters in "chris".
# --------------------------------------------------------------------
#     "A crew that boards the ship", "chris" --> false
#        cr    h              s i
#        cr                h  s i
#        c     h      r       s i
#                  ...
#
#     Contains all of the letters in "chris", but not in order.
# --------------------------------------------------------------------
#     "A live son", "Allison" --> false
#      ^ ^^   ^^^
#      A li   son
#
#     Contains all of the correct letters in "Allison", in order, but not
#     enough of all of them (missing an 'l').


def name_in_str(s: str, name: str) -> bool:
    name = name.lower()
    i = 0
    for letter in s.lower():
        if letter == name[i]:
            if i == len(name) - 1:
                return True
            i += 1
    return False


assert name_in_str("Across the rivers", "chris") is True
assert name_in_str("Next to a lake", "chris") is False
assert name_in_str("Under a sea", "chris") is False
assert name_in_str("thomas", "Thomas") is True
assert name_in_str("pippippi", "Pippi") is True
