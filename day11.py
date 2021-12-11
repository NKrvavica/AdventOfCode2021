# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 07:51:21 2021

@author: Nino
"""
from aoc import *
import numpy as np
from itertools import product


def get_neighbours(y, x):
    y1 = y-1 if (y-1 >= 0) else y
    y2 = y+2 if (y+1 < MAXY) else y+1
    x1 = x-1 if (x-1 >= 0) else x
    x2 = x+2 if (x+1 < MAXX) else x+1
    yy, xx = np.arange(y1, y2), np.arange(x1, x2)
    n_coord = set(product(yy, xx))
    n_coord.remove((y,x))
    return n_coord


# LOAD DATA
# data = read_input('example11')
data = read_input(11)
data_array = np.array([mapl(int, line) for line in data])
MAXY, MAXX = data_array.shape


# MAIN
nr_flashes, step, synced = 0, 0, 0
while not synced:
    step += 1
    flashed = np.zeros_like(data_array).astype(bool)
    data_array += 1
    should_flash = (data_array > 9) & (~flashed)

    while should_flash.any():
        data_array[should_flash] = 0  # flash! ahaaaa!
        flashed[should_flash] = True
        nr_flashes += should_flash.sum()

        # increase energy of neighbours
        for octopus in zip(*np.where(should_flash)):
            for ny, nx in  get_neighbours(*octopus):
                if ~flashed[ny, nx]: data_array[ny, nx] += 1

        # identify neighbours that should flash
        should_flash = (data_array > 9) & (~flashed)

        # condition for part 2
        synced = (True if (data_array == 0).all() else False)

    # part 1 (number of flashes after 100 steps)
    if step == 100:
        p1 = nr_flashes

print(p1)
print(step)
