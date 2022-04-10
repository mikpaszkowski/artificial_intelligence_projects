import numpy
import pygame

from constants import *

pygame.init()
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('TIC TAC TOE - MINIMAX ALGORITHM')


class Board:

    def __init__(self):
        self.board_squares = numpy.zeros((3, 3))
        self.num_of_marked_squares = 0

    def is_over(self, draw_lines=True):
        for num in range(0, 3):
            if self.board_squares[num][0] == self.board_squares[num][1] == self.board_squares[num][2] and \
                    self.board_squares[num][0] != 0:
                if draw_lines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (0, SIZE / 6 * (num * 2 + 1)),
                                     (SIZE, SIZE / 6 * (num * 2 + 1)),
                                     LINE_WIDTH_XO)
                return self.board_squares[num][0]

            if self.board_squares[0][num] == self.board_squares[1][num] == self.board_squares[2][num] and \
                    self.board_squares[0][num] != 0:
                if draw_lines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (SIZE / 6 * (num * 2 + 1), 0),
                                     (SIZE / 6 * (num * 2 + 1), SIZE),
                                     LINE_WIDTH_XO)
                return self.board_squares[0][num]

            if self.board_squares[0][0] == self.board_squares[1][1] == self.board_squares[2][2] and \
                    self.board_squares[0][0] != 0:
                if draw_lines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (0, 0), (SIZE, SIZE), LINE_WIDTH_XO)
                return self.board_squares[1][1]

            if self.board_squares[0][2] == self.board_squares[1][1] == self.board_squares[2][0] and \
                    self.board_squares[0][2] != 0:
                if draw_lines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (0, SIZE), (SIZE, 0), LINE_WIDTH_XO)
                return self.board_squares[1][1]
        return 0

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
