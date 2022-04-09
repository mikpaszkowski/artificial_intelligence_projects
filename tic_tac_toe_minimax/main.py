import sys

import pygame
from pygame import MOUSEBUTTONDOWN

from constants import *

XO = 'x'

board = [[None] * 3,[None] * 3,[None] * 3]

pygame.init()
window = pygame.display.set_mode((SIZE, SIZE))
pygame.display.set_caption('TIC TAC TOE - MINIMAX ALGORITHM')


def show_game_window():
    pygame.display.update()

    pygame.draw.line(window, LINE_COLOR, (SIZE / 3, 0), (SIZE / 3, SIZE), 5)
    pygame.draw.line(window, LINE_COLOR, (SIZE / 3 * 2, 0), (SIZE / 3 * 2, SIZE), 5)

    pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3), (SIZE, SIZE / 3), 5)
    pygame.draw.line(window, LINE_COLOR, (0, SIZE / 3 * 2), (SIZE, SIZE / 3 * 2), 5)


def draw(row, column):
    global XO

    if column == 1:
        x_cor = SIZE / 6
    elif column == 2:
        x_cor = SIZE / 6 * 3
    elif column == 3:
        x_cor = SIZE / 6 * 5

    if row == 1:
        y_cor = SIZE / 6
    elif row == 2:
        y_cor = SIZE / 6 * 3
    elif row == 3:
        y_cor = SIZE / 6 * 5

    board[row - 1][column - 1] = XO

    if XO == 'x':
        pygame.draw.line(window, LINE_COLOR, (x_cor - 50, y_cor + 50), (x_cor + 50, y_cor - 50), 5)
        pygame.draw.line(window, LINE_COLOR, (x_cor - 50, y_cor - 50), (x_cor + 50, y_cor + 50), 5)
        XO = 'o'
    else:
        pygame.draw.circle(window, LINE_COLOR, (x_cor, y_cor), 50, 5)
        XO = 'x'

    pygame.display.update()

def click():
    x, y = pygame.mouse.get_pos()

    if x < SIZE / 3:
        column = 1
    elif x < SIZE / 3 * 2 and x > SIZE / 3:
        column = 2
    else:
        column = 3

    if y < SIZE / 3:
        row = 1
    elif y < SIZE / 3 * 2 and y > SIZE / 3:
        row = 2
    else:
        row = 3

    print("row: ", row)
    print("column: ", column)

    if row and column and board[row - 1][column - 1] is None:
        global XO
        draw(row, column)



def main():
    show_game_window()
    print("fwefwe")

    while 1:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                click()

        pygame.display.update()


main()
