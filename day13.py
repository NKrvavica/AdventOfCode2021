# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:17:29 2021

@author: Nino
"""

from aoc import *
import numpy as np


def parse_input(instruc):
    coords, folds = [], []
    coord_data = True
    for line in instruc:
        if line == '':
            coord_data = False
            continue
        if coord_data:
            x, y = map(int, line.split(','))
            coords.append((y, x))
        else:
            a, b = line.split('=')
            folds.append((a[-1], int(b)))
    coords = np.array(coords)
    maxy, maxx = coords[:, 0].max(), coords[:, 1].max()
    paper = np.zeros((maxy+1, maxx+1), dtype=bool)
    paper[tuple(coords.T)] = 1
    return paper, coords, folds


def fold_paper(paper, fold):
    axis, s = fold
    if axis == 'y':
        pap1, pap2 = paper[:s+1, :], paper[s:, :]
        folded_paper = pap1[:-1, :] + np.flipud(pap2)[:-1, :]
    else:  # x
        pap1, pap2 = paper[:, :s+1], paper[:, s:]
        folded_paper = pap1[:, :-1] + np.fliplr(pap2)[:, :-1]
    return folded_paper


instruc = read_input(13)

paper, coords, folds = parse_input(instruc)

for fold in folds:
    paper = fold_paper(paper, fold)
    dots = paper.sum()

import matplotlib.pyplot as plt
plt.imshow(paper)
