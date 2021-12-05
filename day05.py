# -*- coding: utf-8 -*-
"""
Created on Sun Dec  5 08:35:11 2021

@author: Nino
"""

from aoc import *
import numpy as np


def connect(data, part=1):
    field = np.zeros((1000, 1000))
    for points in data:
        x1, y1, x2, y2 = integers(points)
        if (x1 == x2) or (y1 == y2) or (part==2):
            if x1 < x2:
                xs = np.arange(x1, x2 + 1)
            else:
                xs = np.arange(x1, x2 - 1, -1)
            if y1 < y2:
                ys = np.arange(y1, y2 + 1)
            else:
                ys = np.arange(y1, y2 - 1, -1)
            field[ys, xs] += 1
    return len(field[field >= 2])



data = read_input(5)

p1 = connect(data, part=1)
print(p1)

p2 = connect(data, part=2)
print(p2)
