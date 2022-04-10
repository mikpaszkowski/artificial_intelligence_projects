#import random
import sys
import time

#import numpy
# from numpy import Infinity
import pygame
from pygame import MOUSEBUTTONDOWN

from constants import *
#from board import Board
#from algorithm import Algorithm
from game import Game

winner = None
draw = None








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
                        game.is_running = False

                if game.is_running and game.player == algorithm.player:
                    pygame.display.update()
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

                        game.is_running = False

                    

                pygame.display.update()


main()
