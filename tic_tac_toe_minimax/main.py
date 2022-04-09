import random
import sys
import time

import numpy
import pygame
from pygame import MOUSEBUTTONDOWN

from constants import *

# player 1: 1
# player 2: 2

winner = None
draw = None

pygame.init()
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('TIC TAC TOE - MINIMAX ALGORITHM')


class Board:

    def __init__(self):
        self.board_squares = numpy.zeros((SIZE, SIZE))
        self.num_of_marked_squares = 0

    def is_over(self):
        for num in range(0, 3):
            if self.board_squares[num][0] == self.board_squares[num][1] == self.board_squares[num][2] and \
                    self.board_squares[num][0] != 0:
                pygame.draw.line(window, RESULT_LINE_COLOR, (0, SIZE / 6 * (num * 2 + 1)),
                                 (SIZE, SIZE / 6 * (num * 2 + 1)),
                                 LINE_WIDTH_XO)
                return True

            if self.board_squares[0][num] == self.board_squares[1][num] == self.board_squares[2][num] and \
                    self.board_squares[0][num] != 0:
                pygame.draw.line(window, RESULT_LINE_COLOR, (SIZE / 6 * (num * 2 + 1), 0),
                                 (SIZE / 6 * (num * 2 + 1), SIZE),
                                 LINE_WIDTH_XO)
                return True

            if self.board_squares[0][0] == self.board_squares[1][1] == self.board_squares[2][2] and \
                    self.board_squares[0][0] != 0:
                pygame.draw.line(window, RESULT_LINE_COLOR, (0, 0), (SIZE, SIZE), LINE_WIDTH_XO)
                return True

            if self.board_squares[0][2] == self.board_squares[1][1] == self.board_squares[2][0] and \
                    self.board_squares[0][2] != 0:
                pygame.draw.line(window, RESULT_LINE_COLOR, (0, SIZE), (SIZE, 0), LINE_WIDTH_XO)
                return True
        print("False")
        return False

    def mark_square(self, row, column, player):
        self.board_squares[row][column] = player
        self.num_of_marked_squares += 1

    def is_empty(self, row, column):
        return self.board_squares[row][column] == 0

    def is_board_full(self):
        return self.num_of_marked_squares == 9

    def get_empty_board_squares(self):
        empty_squares = []
        for row in range(3):
            for col in range(3):
                if self.is_empty(row, col):
                    empty_squares.append((row, col))
        return empty_squares


class Algorithm:

    def __init__(self, level=0, player=2):
        self.level = level
        self.player = player

    def random_move(self, board_squares):
        empty_board_squares = board_squares
        # print(empty_board_squares)
        rand = empty_board_squares[random.randrange(0, len(empty_board_squares))]
        print("rand: ", rand)
        return rand

    def evaluate_move(self, board_squares):

        if self.level == 0:
            move = self.random_move(board_squares)
        else:

            pass
        return move


class Game:

    def __init__(self):
        self.board = Board()
        self.algorithm = Algorithm()
        self.player = 1
        self.is_running = True

    def show_game_window(self):
        pygame.display.update()

        window.fill(BACKGROUND_COLOR)

        pygame.draw.line(window, LINE_COLOR, (SIZE / 3, 0), (SIZE / 3, SIZE), LINE_WIDTH_BOARD)
        pygame.draw.line(window, LINE_COLOR, (SIZE / 3 * 2, 0), (SIZE / 3 * 2, SIZE), LINE_WIDTH_BOARD)

        pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3), (SIZE, SIZE / 3), LINE_WIDTH_BOARD)
        pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3 * 2), (SIZE, SIZE / 3 * 2), LINE_WIDTH_BOARD)

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

    def is_game_finshed(self):
        return self.board.is_over() or self.board.is_board_full()


def main():
    game = Game()
    board = game.board
    algorithm = game.algorithm

    game.show_game_window()

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:

                x, y = pygame.mouse.get_pos()

                row = int(y // SQ_SIZE)
                column = int(x // SQ_SIZE)

                if board.is_empty(row, column) and game.is_running:
                    game.move(row, column)

                    if game.is_game_finshed():
                        print("here")
                        game.is_running = False

                if game.is_running and game.player == algorithm.player:
                    pygame.display.update()
                    print("ai before: ", board.get_empty_board_squares())
                    a, b = algorithm.evaluate_move(board.get_empty_board_squares())
                    game.move(a, b)
                    if game.is_game_finshed():

                        game.is_running = False

        pygame.display.update()


main()
