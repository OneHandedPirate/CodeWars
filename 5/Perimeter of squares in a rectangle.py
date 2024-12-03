# The drawing shows 6 squares the sides of which have a length of 1, 1, 2, 3, 5, 8.
# It's easy to see that the sum of the perimeters of these squares is
# : 4 * (1 + 1 + 2 + 3 + 5 + 8) = 4 * 20 = 80
#
# Could you give the sum of the perimeters of all the squares in a rectangle
# when there are n + 1 squares disposed in the same manner as in the drawing:


def perimeter(n: int):
    res = 0
    a, b = 1, 1
    for _ in range(n + 1):
        res += a
        a, b = b, a + b
    return res * 4


assert perimeter(5) == 80
assert perimeter(30) == 14098308
assert perimeter(7) == 216