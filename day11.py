# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 07:51:21 2021

@author: Nino
"""
from aoc import *
import numpy as np
from itertools import product


def load_data(fname):
    data = read_input(fname)
    data_array = np.array([mapl(int, line) for line in data])
    return data_array


def get_neighbours(y, x):
    y1 = y-1 if (y-1 >= 0) else y
    y2 = y+2 if (y+1 < MAXY) else y+1
    x1 = x-1 if (x-1 >= 0) else x
    x2 = x+2 if (x+1 < MAXX) else x+1
    n_coord = set(product(np.arange(y1, y2), np.arange(x1, x2)))
    n_coord.remove((y,x))
    return n_coord


def increase_energy(should_flash, energy_level):
    for octopus in zip(*np.where(should_flash)):
        for neighbour in get_neighbours(*octopus):
            if energy_level[neighbour] > 0: energy_level[neighbour] += 1
    return energy_level


def main(energy_level):
    nr_flashes, step = 0, 0
    while True:

        step += 1
        energy_level += 1
        should_flash = (energy_level > 9)

        while should_flash.any():

            energy_level[should_flash] = 0  # flash! ahaaaa!
            nr_flashes += should_flash.sum()

            # increase energy of neighbours
            energy_level = increase_energy(should_flash, energy_level)

            # identify neighbours that should flash
            should_flash = (energy_level > 9)

        # part 1 (number of flashes after 100 steps)
        if step == 100:
            p1 = nr_flashes

        # part 2 (sync)
        if (energy_level == 0).all():
            return p1, step


energy_level = load_data(11)
MAXY, MAXX = energy_level.shape
p1, p2 = main(energy_level)
print(p1)
print(p2)
