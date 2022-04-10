import copy
import random
import sys
import time

import numpy
from numpy import Infinity
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
        self.board_squares = numpy.zeros((3,3))
        self.num_of_marked_squares = 0

    def is_over(self, drawLines = True):
        for num in range(0, 3):
            if self.board_squares[num][0] == self.board_squares[num][1] == self.board_squares[num][2] and \
                    self.board_squares[num][0] != 0:
                if drawLines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (0, SIZE / 6 * (num * 2 + 1)),
                                 (SIZE, SIZE / 6 * (num * 2 + 1)),
                                 LINE_WIDTH_XO)
                return self.board_squares[num][0]

            if self.board_squares[0][num] == self.board_squares[1][num] == self.board_squares[2][num] and \
                    self.board_squares[0][num] != 0:
                if drawLines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (SIZE / 6 * (num * 2 + 1), 0),
                                 (SIZE / 6 * (num * 2 + 1), SIZE),
                                 LINE_WIDTH_XO)
                return self.board_squares[0][num]

            if self.board_squares[0][0] == self.board_squares[1][1] == self.board_squares[2][2] and \
                    self.board_squares[0][0] != 0:
                if drawLines:
                    pygame.draw.line(window, RESULT_LINE_COLOR, (0, 0), (SIZE, SIZE), LINE_WIDTH_XO)
                return self.board_squares[1][1]

            if self.board_squares[0][2] == self.board_squares[1][1] == self.board_squares[2][0] and \
                    self.board_squares[0][2] != 0:
                if drawLines:
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


class Algorithm:

    def __init__(self, depth=1, player=2):
        self.depth = depth
        self.player = player

    def random_move(self, board_squares):
        empty_board_squares = board_squares
        print("len(empty_board_squares: ", len(empty_board_squares))
        if len(empty_board_squares) == 0:
            print("bbbbb")
            return None
        return empty_board_squares[random.randrange(0, len(empty_board_squares))]

    def check_terminal_cases(self, board):

        final_result = board.is_over(False)

        if final_result == 1:
            return -1, None

        if final_result == 2:
            return 1, None

        if board.is_board_full():
            return 0, None


    def minimax(self, board, maximizing_player, alpha = -Infinity, beta = Infinity):
        #print("i: ", i)
        result = self.check_terminal_cases(board)

        if result is not None:
            # print("it'll be a tie")
            # a = [-1, -1]
            return result#float(0), a

        #temp_board = copy.deepcopy(board)
        if maximizing_player:
            max_eval = -Infinity
            move = None
            empty_squares = board.get_empty_board_squares()

            for (row, column) in empty_squares:
                # print("\nbefore: ", temp_board.get_empty_board_squares())
                # print("mark square: ", row, column)
                board.mark_square(row, column, self.player)
                # print("after: ", temp_board.get_empty_board_squares())
                evaluation = self.minimax(board, False, alpha, beta)[0]
                board.mark_square(row, column, 0)

                if evaluation > max_eval:
                    max_eval = evaluation
                    move = (row, column)
                alpha = max (alpha,max_eval)
                if beta <= alpha:
                    break
            return max_eval, move

        elif not maximizing_player:
            min_eval = +Infinity
            move = None
            empty_squares = board.get_empty_board_squares()

            for (row, column) in empty_squares:
                # print("\nbefore: ", temp_board.get_empty_board_squares())
                # print("mark square: ", row, column)
                board.mark_square(row, column, self.player)
                # print("after: ", temp_board.get_empty_board_squares())
                evaluation = self.minimax(board, True, alpha, beta)[0]
                board.mark_square(row, column, 0)

                if evaluation < min_eval:
                    min_eval = evaluation
                    move = (row, column)
                beta = min( beta, min_eval)
                if beta <= alpha:
                    break
                # print("min_eval, move: ", min_eval, move)
            return min_eval, move

    def evaluate_move(self, board):

        if self.depth == 0:
            move = self.random_move(board.get_empty_board_squares())
        else:
            eval, move = self.minimax(board, False)
        print("move: ", move)
        if move == None:
            print ("aaaa")
            move = self.random_move(board.get_empty_board_squares());
            print("new move: ", move)
        return move


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

                    if game.is_game_finished():
                        # print("here")
                        game.is_running = False

                if game.is_running and game.player == algorithm.player:
                    pygame.display.update()
                    # print("ai before: ", board.get_empty_board_squares())
                    start = time.time()
                    ret = algorithm.evaluate_move(board)
                    end = time.time()
                    print("computed in: ", end-start)
                    if ret != None:
                        a,b = ret
                        end  = time.time()
                        game.move(a, b)
                        if game.is_game_finished():
                            game.is_running = False
                    else:
                        print("no more squares")

                    

                pygame.display.update()


main()
