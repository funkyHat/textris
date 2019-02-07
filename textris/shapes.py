
from random import choice

import board


def shape(*coords):
    shape = board.Board((4, 4))
    for coord in coords:
        shape[coord] = 1
    return shape


line = shape((1, 0), (1, 1), (1, 2), (1, 3))
square = shape((1, 1), (1, 2), (2, 1), (2, 2))
s1 = shape((0, 1), (1, 1), (1, 2), (2, 2))
s2 = shape((0, 2), (1, 2), (1, 1), (2, 1))
l1 = shape((0, 1), (0, 2), (1, 1), (2, 1))
l2 = shape((0, 1), (0, 2), (1, 2), (2, 2))
t = shape((0, 1), (1, 1), (2, 1), (1, 2))


shapes = [line, square, s1, s2, l1, l2, t]


def get_shape():
    return choice(shapes)
