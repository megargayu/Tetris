from piece import Piece
from vars import BOARD_WIDTH, BLANK, BOARD_HEIGHT, Grid, BLOCK, Positions, Locked


def create_grid(locked_positions: Locked) -> Grid:
    grid = [[BLANK for _ in range(BOARD_WIDTH)] for _ in range(BOARD_HEIGHT)]

    for i in range(BOARD_HEIGHT):
        for j in range(BOARD_WIDTH):
            if (j, i) in locked_positions:
                c = locked_positions[(j, i)]
                grid[i][j] = c
    return grid


def convert_piece_format(piece: Piece) -> Positions:
    positions = []

    for i, line in enumerate(piece.to_string()):
        row = list(line)
        for j, column in enumerate(row):
            if column == BLOCK:
                positions.append((piece.x + j, piece.y + i))

    for i, pos in enumerate(positions):
        positions[i] = (pos[0] - 2, pos[1] - 4)

    return positions


def valid_space(piece: Piece, grid: Grid) -> bool:
    accepted_positions = [[(j, i) for j in range(BOARD_WIDTH) if grid[i][j] == BLANK] for i in range(BOARD_HEIGHT)]
    accepted_positions = [j for sub in accepted_positions for j in sub]
    formatted = convert_piece_format(piece)

    for pos in formatted:
        if pos not in accepted_positions and pos[1] > -1:
            return False

    return True


def check_lost(positions: Positions) -> bool:
    for pos in positions:
        x, y = pos
        if y < 1:
            return True
    return False


def clear_rows(grid: Grid, locked: Locked) -> int:
    inc, ind = 0, 0
    for i in range(len(grid) - 1, -1, -1):
        row = grid[i]
        if BLANK not in row:
            inc += 1
            ind = i
            for j in range(len(row)):
                if (j, i) in locked:
                    del locked[(j, i)]
    if inc > 0:
        for key in sorted(list(locked), key=lambda x: x[1])[::-1]:
            if key[1] < ind:
                newKey = (key[0], key[1] + inc)
                locked[newKey] = locked.pop(key)
    return inc
