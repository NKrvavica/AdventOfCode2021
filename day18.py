# -*- coding: utf-8 -*-
"""
Created on Fri Dec 17 08:13:25 2021

@author: Nino
"""

import numpy as np


def fly(pos, v):
    t = 0
    maxh = 0
    in_air = True
    while in_air:
        t += 1
        pos += v
        maxh = max(maxh, pos[1])
        if ((xtarget[0] <= pos[0] <=xtarget[1])
            and (ytarget[0] <= pos[1] <=ytarget[1])):
            return 'pogodio', maxh
        elif (pos[1] < ytarget[0]):
            if pos[0] < xtarget[0]:
                return 'preslabo', None
            elif (xtarget[0] <= pos[0] <=xtarget[1]):
                return 'prejako', None
            else:
                return 'predaleko', None
        v[0] = np.sign(v[0]) * (abs(v[0]) - 1)
        v[1] -= 1


def main(xtarget, ytarget):
    pos = np.array([0, 0])
    v = np.array([1, ytarget[0]])
    reached = False
    hits = set()
    maxheight = 0
    while True:
        hit, maxh = fly(pos.copy(), v.copy())
        # print(v, hit)
        if hit == 'pogodio':
            reached = True
            hits.add(tuple(v))
            maxheight = max(maxheight, maxh)
            v[0] += 1
        elif hit == 'predaleko' and v[0] > xtarget[0]:
            v[1] += 1
            v[0] = 1
            if not reached and v[1] > 0:
                return maxheight, hits
            else:
                reached = False
        elif hit == 'prejako' and v[0] > xtarget[0]:
            v[1] += 1
        else:
            v[0] += 1


# example
# xtarget = (20, 30)
# ytarget = (-10, -5)

# My input
# target area: x=195..238, y=-93..-67
xtarget = (195, 238)
ytarget = (-93, -67)

maxheight, hits = main(xtarget, ytarget)

print(maxheight)
print(len(hits))
