# Your job is to write a function which increments a string, to create a new string.
#
# If the string already ends with a number, the number should be incremented by 1.
# If the string does not end with a number. the number 1 should be appended to
# the new string.
# Examples:
#
# foo -> foo1
#
# foobar23 -> foobar24
#
# foo0042 -> foo0043
#
# foo9 -> foo10
#
# foo099 -> foo100
#
# Attention: If the number has leading zeros the amount of digits should be
# considered.


#first ugly solution
# def increment_string(string: str) -> str:
#     if not string or not string[-1].isdigit():
#         return string + "1"
#     tail = ''
#     for c in string[::-1]:
#         if c.isdigit():
#             tail += c
#             continue
#         break
#     tail = tail[::-1]
#     num_tail = int(tail)
#     leading_zeroes_count = len(tail) - len(str(num_tail + 1))
#     return string[:-len(tail)] + leading_zeroes_count * "0" + str(num_tail + 1)

def increment_string(string: str) -> str:
    head = string.rstrip('0123456789')
    tail = string[len(head):]
    if tail == "":
        return string + "1"
    return head + str(int(tail) + 1).zfill(len(tail))


assert increment_string("foobar001") == "foobar002"
assert increment_string("foobar00") == "foobar01"
assert increment_string("") == "1"
assert increment_string("009") == "010"
