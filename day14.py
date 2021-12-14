# -*- coding: utf-8 -*-
"""
Created on Mon Dec 13 08:17:29 2021

@author: Nino
"""

from aoc import *
from itertools import product
from collections import defaultdict


def parse_input(data):
    template, str_rules = map(str.splitlines, data)
    template = template[0]
    rules = defaultdict(str)
    for line in str_rules:
        k, v = line.split(' -> ')
        rules[k] = v
    return template, rules


def pair_dict_from_str(string):
    a = defaultdict(int)
    for i in range(len(string)-1):
        a[string[i:i+2]] += 1
    return a


def insertion(template, rules, N):
    a = pair_dict_from_str(template)
    for step in range(N):
        b = a.copy()
        for k in a:
            if a[k] > 0:
                repeates = a[k]
                insertion = rules[k]
                b[k] -= a[k]
                first = cat((k[0], insertion))
                second = cat((insertion, k[1]))
                b[first] += repeates
                b[second] += repeates
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
a = insertion(template, rules, 40)
res = difference(a, template)
print(res)
