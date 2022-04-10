
import random
# import sys
# import time

# import numpy
from numpy import Infinity
# import pygame
from pygame import MOUSEBUTTONDOWN

from constants import *





class Algorithm:

    def __init__(self, depth=1, player=2):
        self.depth = depth
        self.player = player

    def random_move(self, board_squares):
        empty_board_squares = board_squares
        print("len(empty_board_squares: ", len(empty_board_squares))
        if len(empty_board_squares) == 0:
            return None
        return empty_board_squares[random.randrange(0, len(empty_board_squares))]

    def check_terminal_cases(self, board):

        final_result = board.is_over(False) #is_over checks if one of the players won the game

        if final_result == 1:
            return -1, None #if minimizing player won

        if final_result == 2:
            return 1, None #if maximizing player won

        if board.is_board_full():
            return 0, None


    def minimax(self, board, maximizing_player, alpha = -Infinity, beta = Infinity):
        result = self.check_terminal_cases(board) 
        if result is not None: #if in this configuration someone wins
            return result

        if maximizing_player:       #if the current player is the maximising player
            max_eval = -Infinity    #check possible moves and choose the one with the biggest score
            move = None
            empty_squares = board.get_empty_board_squares()

            for (row, column) in empty_squares:
                board.mark_square(row, column, self.player)
                evaluation = self.minimax(board, False, alpha, beta)[0]
                board.mark_square(row, column, 0)

                if evaluation > max_eval:
                    max_eval = evaluation
                    move = (row, column)
                alpha = max (alpha,max_eval)
                if beta <= alpha:   #if the bigest score in this case is smaller than the smallest score in it's parent
                    break           #don't bother checking
            return max_eval, move

        else:                       #if the current player is the minimizing player
            min_eval = +Infinity    #check possible moves and choose the one with the lowest score
            move = None
            empty_squares = board.get_empty_board_squares()

            for (row, column) in empty_squares:
                board.mark_square(row, column, self.player)
                evaluation = self.minimax(board, True, alpha, beta)[0]
                board.mark_square(row, column, 0)

                if evaluation < min_eval:
                    min_eval = evaluation
                    move = (row, column)
                beta = min( beta, min_eval)
                if beta <= alpha:   #if the smallest score in this case is bigger than the biggest score in parent
                    break           #don't bother checking
            return min_eval, move

    def evaluate_move(self, board):

        if self.depth == 0:
            move = self.random_move(board.get_empty_board_squares())
        else:
            eval,move = self.minimax(board, False)
        print("move: ", move)
        if move == None:
            move = self.random_move(board.get_empty_board_squares());
            print("new move: ", move)
        return move
