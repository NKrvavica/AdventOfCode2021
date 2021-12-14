# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:17:29 2021

@author: Nino
"""

from aoc import *
from itertools import product
from collections import defaultdict, Counter


def parse_input(data):
    template, str_rules = map(str.splitlines, data)
    rules = dict(r.split(' -> ') for r in str_rules)
    return template[0], rules


def insertion(template, rules, N):
    a = Counter(template[i:i+2] for i in range(len(template)-1))
    for step in range(N):
        b = a.copy()
        for k in a:
            if a[k] > 0:
                repeates = a[k]
                insertion = rules[k]
                b[k] -= a[k]
                b[cat((k[0], insertion))] += repeates
                b[cat((insertion, k[1]))] += repeates
        a = b
    return a


def difference(a, template):
    nr_letters = defaultdict(int)
    nr_letters[template[-1]] = 1 # last letter from the input
    for k in a:
        nr_letters[k[0]] += a[k]  # count only the first letter in each pair
    return max(nr_letters.values()) - min(nr_letters.values())


# data = read_input('example14', sep='\n\n')
data = read_input(14, sep='\n\n')
template, rules = parse_input(data)

a = insertion(template, rules, 10)
p1 = difference(a, template)<
print(p1)

a = insertion(template, rules, 40)
p2 = difference(a, template)
print(p2)
