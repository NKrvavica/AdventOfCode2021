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
            dx, dy = abs(x1 - x2), abs(y1 - y2)
            xs = np.linspace(x1, x2, dx + 1).astype(int)
            ys = np.linspace(y1, y2, dy + 1).astype(int)
            field[ys, xs] += 1
    return (field >= 2).sum()

data = read_input(5)

p1 = connect(data, part=1)
print(p1)

p2 = connect(data, part=2)
print(p2)
