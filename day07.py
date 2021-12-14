# -*- coding: utf-8 -*-
"""
Created on Tue Dec  7 08:18:24 2021

@author: Nino
"""

import numpy as np

positions = np.array([16,1,2,0,4,2,7,1,2,14])
positions.mean()

positions = np.loadtxt('./inputs/day07.txt', delimiter=',').astype(int)


def triangular(n):
    return n * (n + 1) // 2

def cheapest(positions, part=1):
    min_fuel = np.inf
    for i in range(max(positions)):
        if part == 1:
            fuel = abs(positions - i).sum()
        else:
            fuel = triangular(abs(positions - i)).sum()
        min_fuel = min(fuel, min_fuel)
    return min_fuel


p1 = cheapest(positions, part=1)
print(p1)

p2 = cheapest(positions, part=2)
print(p2)
