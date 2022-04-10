# import random
# import sys
# import time

# import numpy
from numpy import Infinity
import pygame
from pygame import MOUSEBUTTONDOWN

from constants import *
from board import Board
from algorithm import Algorithm



pygame.init()
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('TIC TAC TOE - MINIMAX ALGORITHM')

class Game:

    def __init__(self):
        self.board = Board()
        self.algorithm = Algorithm()
        self.player = 1
        self.is_running = True

    def show_game_window(self):

        window.fill(BACKGROUND_COLOR)

        pygame.draw.line(window, LINE_COLOR, (SIZE / 3, 0), (SIZE / 3, SIZE), LINE_WIDTH_BOARD)
        pygame.draw.line(window, LINE_COLOR, (SIZE / 3 * 2, 0), (SIZE / 3 * 2, SIZE), LINE_WIDTH_BOARD)

        pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3), (SIZE, SIZE / 3), LINE_WIDTH_BOARD)
        pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3 * 2), (SIZE, SIZE / 3 * 2), LINE_WIDTH_BOARD)

        pygame.display.update()

    def draw(self, row, column):

        if column == 0:
            x_cor = SIZE / 6
        elif column == 1:
            x_cor = SIZE / 6 * 3
        else:
            x_cor = SIZE / 6 * 5

        if row == 0:
            y_cor = SIZE / 6
        elif row == 1:
            y_cor = SIZE / 6 * 3
        else:
            y_cor = SIZE / 6 * 5

        if self.player == 1:
            pygame.draw.line(window, COLOR_X, (x_cor - WIDTH_FIG_X, y_cor + WIDTH_FIG_X),
                             (x_cor + WIDTH_FIG_X, y_cor - WIDTH_FIG_X), LINE_WIDTH_XO)
            pygame.draw.line(window, COLOR_X, (x_cor - WIDTH_FIG_X, y_cor - WIDTH_FIG_X),
                             (x_cor + WIDTH_FIG_X, y_cor + WIDTH_FIG_X), LINE_WIDTH_XO)
        else:
            pygame.draw.circle(window, COLOR_O, (x_cor, y_cor), RADIUS_FIG_O, LINE_WIDTH_XO)

        pygame.display.update()

    def move(self, row, col):
        self.board.mark_square(row, col, self.player)
        self.draw(row, col)
        self.next_player()

    def next_player(self):
        self.player = self.player % 2 + 1

    def is_game_finished(self):
        return self.board.is_over() != 0 or self.board.is_board_full()
