# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 08:42:28 2021

@author: Nino
"""

from aoc import *
import networkx as nx
from collections import deque, Counter


def find_paths(G, source, target, part=1):
    paths = 0
    visited = deque([source])
    if part == 2:
        visited.append(source)
    stack = [deque(G.neighbors(source))]
    while stack:

        children = stack[-1]
        if children:
            child = children.pop()
        else:
            stack.pop()
            visited.pop()
            continue

        if child == target:
            # print('found link: ', list(visited) + [target])
            paths += 1
        else:
            values_dict = Counter(visited)
            twice = True
            if part == 2:
                for key in values_dict:
                    if (key.islower()
                        and key != source
                        and values_dict[key] == 2):
                        twice = False
            if (child not in visited or child.isupper()
                or (Counter(visited)[child] == 1
                    and twice
                    and part == 2)):
                visited.append(child)
                stack.append(deque(G.neighbors(child)))
    return paths


data = read_input(12)

G = nx.Graph()
for connection in data:
    G.add_edge(*connection.split('-'))

p1 = find_paths(G, source='start', target='end', part=1)
print(p1)

p2 = find_paths(G, source='start', target='end', part=2)
print(p2)


import matplotlib.pyplot as plt

subax1 = plt.subplot()
nx.draw(G, with_labels=True, font_weight='bold')
