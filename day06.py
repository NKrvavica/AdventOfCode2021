# -*- coding: utf-8 -*-
"""
Created on Mon Dec  6 07:55:36 2021

@author: Nino
"""

import numpy as np

# fishes = np.array([3,4,3,1,2])

fishes = np.loadtxt('./inputs/day06.txt', delimiter=',').astype(int)


def spawn(days, fishes):
    fish_ages = np.zeros(9).astype('longlong')
    for fish_age in fishes:
        fish_ages[fish_age] += 1
    for day in range(days):
        fish_ages = np.roll(fish_ages, -1)
        fish_ages[6] += fish_ages[8]  # parents
    return fish_ages.sum().astype('longlong')


print(spawn(80, fishes))

print(spawn(256, fishes))
