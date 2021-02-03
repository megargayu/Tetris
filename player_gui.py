import random

import pygame
import os

from grid import create_grid, valid_space, convert_piece_format, clear_rows, check_lost
from piece import get_random_piece
from vars import SHAPE_COLORS, BOARD_HEIGHT, BOARD_WIDTH, BLANK, FALL_SPEED, SHAPES_TRIM, FAST_FALL_SPEED, \
    SCORE_PER_LINE


def draw_board(screen, board):
    def _draw_square(pos, color):
        pygame.draw.rect(screen, color, pygame.Rect(105 + pos[0] * 30, 50 + pos[1] * 30, 30, 30))

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[y][x] != BLANK:
                _draw_square((x, y), SHAPE_COLORS[board[y][x]])
    pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(105, 50, 300, 600), 4)


def draw_info(screen, lines, score, next_piece):
    def _draw_next_board():
        for x in range(2):
            for y in range(4):
                if SHAPES_TRIM[next_piece.shape_str][x][y] != BLANK:
                    pygame.draw.rect(screen, SHAPE_COLORS[next_piece.shape_str],
                                     pygame.Rect(457 + y * 35, 105 + x * 35, 35, 35))

        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(457, 105, 140, 70), 3)

    def _draw_text(string, center, font_size):
        font = pygame.font.Font('fonts/pixeled.ttf', font_size)
        text = font.render(string, False, (255, 255, 255))
        textRect = text.get_rect()
        textRect.center = center
        screen.blit(text, textRect)

    _draw_text("NEXT", (532, 70), 25)
    _draw_next_board()

    _draw_text("SCORE", (532, 230), 20)
    _draw_text(str(score), (532, 265), 16)

    _draw_text("LINES", (532, 320), 17)
    _draw_text(str(lines), (532, 355), 13)


def init_music():
    if random.randint(0, 1) == 0:
        pygame.mixer.music.load('music/tetris1.mid')
    else:
        pygame.mixer.music.load('music/tetris2.mid')
    pygame.mixer.music.play(-1, 0.0)


def run():
    locked_positions = {}

    change_piece = False
    current_piece = get_random_piece()
    next_piece = get_random_piece()
    clock = pygame.time.Clock()
    lines, score = 0, 0
    fall_time = 0

    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Tetris")
    init_music()

    while True:
        grid = create_grid(locked_positions)
        fall_time += clock.get_rawtime()
        clock.tick()

        pressed_keys = pygame.key.get_pressed()
        if fall_time / 1000 >= (FAST_FALL_SPEED if pressed_keys[pygame.K_DOWN] else FALL_SPEED):
            fall_time = 0
            current_piece.y += 1
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True
            else:
                score += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    current_piece.x -= 1
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1

                elif event.key == pygame.K_RIGHT:
                    current_piece.x += 1
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1

                elif event.key == pygame.K_UP:
                    current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)

                if event.key == pygame.K_SPACE:
                    while valid_space(current_piece, grid):
                        current_piece.y += 1
                        score += 2
                    current_piece.y -= 1
                    score -= 2

        shape_pos = convert_piece_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:
                grid[y][x] = current_piece.shape_str

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.shape_str
            current_piece = next_piece
            next_piece = get_random_piece()
            change_piece = False

            lines_cleared = clear_rows(grid, locked_positions)
            lines += lines_cleared
            score += SCORE_PER_LINE[lines_cleared] if lines_cleared <= 3 else (lines_cleared - 2) * SCORE_PER_LINE[3]

        screen.fill((0, 0, 0))
        draw_board(screen, grid)
        draw_info(screen, lines, score, next_piece)
        pygame.display.update()

        if check_lost(locked_positions):
            pygame.quit()
            quit()


if __name__ == "__main__":
    run()
