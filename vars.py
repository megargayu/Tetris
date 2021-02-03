from typing import List, Dict, Tuple, NewType

# Types
Color = NewType("Color", Tuple[int, int, int])
Grid = NewType("Grid", List[List[str]])
Shape = NewType("Shape", List[List[str]])

# FOR GRID.PY
Positions = NewType("Positions", List[Tuple[int, int]])
Locked = NewType("Locked", Dict[Tuple[int, int], str])

# Scoring system (based on # of lines cleared in a row)
SCORE_PER_LINE: List[int] = [0, 100, 300, 500]

# Board variables
BOARD_WIDTH: int = 10
BOARD_HEIGHT: int = 20

# Timing variables
FALL_SPEED: float = 0.27
FAST_FALL_SPEED: float = 0.05

# All types of shapes
SHAPE_TYPES: List[str] = [
    'S', 'Z', 'I', 'O', 'J', 'L', 'T'
]

# Contains all pieces + rotations
BLOCK: str = 'O'
BLANK: str = '.'
S_SHAPE_TEMPLATE: Shape = [['.....',
                            '.....',
                            '..OO.',
                            '.OO..',
                            '.....'],
                           ['.....',
                            '..O..',
                            '..OO.',
                            '...O.',
                            '.....']]

Z_SHAPE_TEMPLATE: Shape = [['.....',
                            '.....',
                            '.OO..',
                            '..OO.',
                            '.....'],
                           ['.....',
                            '..O..',
                            '.OO..',
                            '.O...',
                            '.....']]

I_SHAPE_TEMPLATE: Shape = [['..O..',
                            '..O..',
                            '..O..',
                            '..O..',
                            '.....'],
                           ['.....',
                            '.....',
                            'OOOO.',
                            '.....',
                            '.....']]

O_SHAPE_TEMPLATE: Shape = [['.....',
                            '.....',
                            '.OO..',
                            '.OO..',
                            '.....']]

J_SHAPE_TEMPLATE: Shape = [['.....',
                            '.O...',
                            '.OOO.',
                            '.....',
                            '.....'],
                           ['.....',
                            '..OO.',
                            '..O..',
                            '..O..',
                            '.....'],
                           ['.....',
                            '.....',
                            '.OOO.',
                            '...O.',
                            '.....'],
                           ['.....',
                            '..O..',
                            '..O..',
                            '.OO..',
                            '.....']]

L_SHAPE_TEMPLATE: Shape = [['.....',
                            '...O.',
                            '.OOO.',
                            '.....',
                            '.....'],
                           ['.....',
                            '..O..',
                            '..O..',
                            '..OO.',
                            '.....'],
                           ['.....',
                            '.....',
                            '.OOO.',
                            '.O...',
                            '.....'],
                           ['.....',
                            '.OO..',
                            '..O..',
                            '..O..',
                            '.....']]

T_SHAPE_TEMPLATE: Shape = [['.....',
                            '..O..',
                            '.OOO.',
                            '.....',
                            '.....'],
                           ['.....',
                            '..O..',
                            '..OO.',
                            '..O..',
                            '.....'],
                           ['.....',
                            '.....',
                            '.OOO.',
                            '..O..',
                            '.....'],
                           ['.....',
                            '..O..',
                            '.OO..',
                            '..O..',
                            '.....']]

SHAPES: Dict[str, Shape] = {'S': S_SHAPE_TEMPLATE,
                            'Z': Z_SHAPE_TEMPLATE,
                            'J': J_SHAPE_TEMPLATE,
                            'L': L_SHAPE_TEMPLATE,
                            'I': I_SHAPE_TEMPLATE,
                            'O': O_SHAPE_TEMPLATE,
                            'T': T_SHAPE_TEMPLATE}

# For held and next pieces ("trimmed" shapes)
SHAPES_TRIM: Dict[str, List[str]] = {'S': ['.OO.',
                                           'OO..'],
                                     'Z': ['OO..',
                                           '.OO.'],
                                     'J': ['OOO.',
                                           '..O.'],
                                     'L': ['..O.',
                                           'OOO.'],
                                     'I': ['....',
                                           'OOOO'],
                                     'O': ['.OO.',
                                           '.OO.'],
                                     'T': ['OOO.',
                                           '.O..']}

# Colors of all shapes
SHAPE_COLORS: Dict[str, Color] = {
    "S": (0, 255, 0),
    "Z": (255, 0, 0),
    "I": (0, 255, 255),
    "O": (255, 255, 0),
    "J": (255, 165, 0),
    "L": (0, 0, 255),
    "T": (128, 0, 128)
}
