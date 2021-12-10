# -*- coding: utf-8 -*-
"""
Created on Fri Dec 10 07:54:16 2021

@author: Nino
"""
from aoc import *
from collections import deque


LEFT = {'(', '[', '{', '<'}
RIGHT = {')', ']', '}', '>'}
PAIRS = {'(': ')', '[': ']', '{': '}', '<': '>'}

ERRORPOINTS = {')': 3, ']': 57, '}': 1197, '>': 25137}
POINTS = {')': 1, ']': 2, '}': 3, '>': 4}


def analyse(line):
    processed_line = deque()
    for c in line:
        if c in LEFT:
            processed_line.extend(c)
        elif c in RIGHT:
            if PAIRS[processed_line[-1]] == c:
                processed_line.pop()
            else:  # error
                return processed_line, c
    return processed_line, None


def repair(processed_line):
    to_complete = []
    while len(processed_line) > 0:
        to_complete.append(PAIRS[processed_line[-1]])
        processed_line.pop()
    return to_complete


def comp_error(wrong_char):
    return sum(ERRORPOINTS[c] for c in wrong_char)


def comp_total_points(to_complete):
    score = 0
    for c in to_complete:
        score *= 5
        score += POINTS[c]
    return score


# data = read_input('example10')
data = read_input(10)

points, wrong_char = [], []
for line in data:
    processed_line, c = analyse(line)
    if c:  # part 1
        wrong_char.append(c)
    else:  # part 2
        points.append(comp_total_points(repair(processed_line)))

# part 1
print(comp_error(wrong_char))

# part 2
print(sorted(points)[len(points)//2])
