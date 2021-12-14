# -*- coding: utf-8 -*-
"""
Created on Sat Dec  4 08:27:09 2021

@author: Nino
"""

import numpy as np


def load_input(fname):
    # load numbers from the first row
    numbers = np.loadtxt(fname, delimiter=',', max_rows=2)
    # load boards
    boards = np.loadtxt(fname, skiprows=2)
    # reshape boards into 3d array (board, row, col)
    n_rows, n_cols = boards.shape
    n_boards = n_rows // n_cols
    # assume that boards are square
    boards = np.reshape(boards, (n_boards, n_cols, n_cols))
    return numbers, boards


def play_bingo(numbers, boards, first_board_wins=True):
    # total number of boards
    n_boards = boards.shape[0]
    # init winning boards
    boards_won = set()
    # draw numbers
    for nr in numbers:
        # check the board for the drawn number (mark that numberin all boards)
        boards[boards == nr] = np.nan
        # check rows then columns (rows axis=1, columns axis=2)
        for i in range(2):
            # check if any row/column is completed
            check =  np.isnan(boards).all(axis=i+1)
            if check.any():
                # index(ices) of the completed board
                board_idx, _ = np.where(check)
                boards_won.update(board_idx)
                print(f'number {nr}, bingo! board(s) {board_idx} completed...')
                # compute the score
                score = np.nansum(boards[board_idx, :, :]) * nr
                if first_board_wins:
                    return score
                # remove the board from play
                boards[board_idx, :, :] = -9999
        if len(boards_won) == n_boards: # last winning board
            return score
    return score  # this should not happen (all numbers are drawn)


numbers, boards = load_input('./inputs/day04.txt')

p1 = play_bingo(numbers, boards.copy())
print(int(p1))

p2 = play_bingo(numbers, boards.copy(), first_board_wins=False)
print(int(p2))
