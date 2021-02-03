import random

from vars import SHAPES, SHAPE_COLORS, SHAPE_TYPES


class Piece(object):
    def __init__(self, col: int, row: int, shape: str):
        self.x = col
        self.y = row
        self.shape_str = shape
        self.shape = SHAPES[shape]
        self.color = SHAPE_COLORS[shape]
        self.rotation = 0

    def to_string(self) -> str:
        return self.shape[self.rotation % len(self.shape)]

    def __str__(self) -> str:
        return 'Piece[type=%s, pos=(%s, %s), rotation=%s]' % (self.shape_str, self.x, self.y, self.rotation)


def get_random_piece() -> Piece:
    return Piece(5, 0, random.choice(SHAPE_TYPES))


def reset_piece(piece: Piece) -> None:
    piece.x = 5
    piece.y = 0
