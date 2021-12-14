# -*- coding: utf-8 -*-
"""
Created on Thu Dec  9 08:00:23 2021

@author: Nino
"""

import numpy as np
from aoc import *


def get_neighbours(y, x):
    n_coord = set()
    if y-1 >= 0: n_coord.add((y-1, x))
    if y+1 < MAXY: n_coord.add((y+1, x))
    if x-1 >= 0: n_coord.add((y, x-1))
    if x+1 < MAXX: n_coord.add((y, x+1))
    return n_coord


def part1(data_array):
    low_points, risk = set(), 0
    for y, x in zip(*np.where(data_array>=0)):
        min_neighbour = min(data_array[neighbour]
                            for neighbour in get_neighbours(y, x))
        if data_array[y, x] < min_neighbour:
            low_points.add((y, x))
            risk += (1 + data_array[y, x])
    return low_points, risk



def should_i_go_there(coord, been_there):
    return (data_array[coord] < 9 and (coord not in been_there))


def part2(data_array, low_points):
    sizes = []
    for y, x in low_points:
        been_there = set()
        to_go = {(y, x)}
        while len(to_go) > 0:
            goy, gox = to_go.pop()
            been_there.add((goy, gox))
            for neighbour in get_neighbours(goy, gox):
                if should_i_go_there(neighbour, been_there):
                    to_go.add(neighbour)
        sizes.append(len(been_there))
    return np.prod(sorted(sizes)[-3:])


# LOAD DATA
# data = read_input('example09')
data = read_input(9)
data_array = np.array([mapl(int, line) for line in data])
MAXY, MAXX = data_array.shape

low_points, risk = part1(data_array)
print(risk)

p2 = part2(data_array, low_points)
print(p2)

# =============================================================================
# PLOT
# =============================================================================
import matplotlib.pyplot as plt
data_array = data_array.astype(float)
data_array[data_array==9] = np.nan
plt.imshow(data_array)
