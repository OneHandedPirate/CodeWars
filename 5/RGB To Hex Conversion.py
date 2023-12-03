# The rgb function is incomplete. Complete it so that passing in RGB decimal
# values will result in a hexadecimal representation being returned. Valid decimal
# values for RGB are 0 - 255. Any values that fall out of that range must be
# rounded to the closest valid value.
#
# Note: Your answer should always be 6 characters long, the shorthand with
# 3 will not work here.
#
# Examples (input --> output):
# 255, 255, 255 --> "FFFFFF"
# 255, 255, 300 --> "FFFFFF"
# 0, 0, 0       --> "000000"
# 148, 0, 211   --> "9400D3"


def rgb(r: int, g: int, b: int) -> str:
    return "".join(map(lambda x: hex(x)[2:].upper().zfill(2) if 0 <= x <= 255 else "00" if x < 0 else "FF", [r, g, b]))


assert rgb(0, 0, 0) == "000000"
assert rgb(1, 2, 3) == "010203"
assert rgb(255, 255, 255) == "FFFFFF"
assert rgb(-20, 275, 125) == "00FF7D"
