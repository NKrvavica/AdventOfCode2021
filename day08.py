# -*- coding: utf-8 -*-
"""
Created on Wed Dec  8 07:57:40 2021

@author: Nino
"""

from aoc import *
from collections import defaultdict

'''
7-segment display:
 aaaa
b    c
b    c
 dddd
e    f
e    f
 gggg
 '''


def unique_char(string_list):
    ''' Return a set of unique letters for a list of strings:
        ['abc', 'adg'] -> {'a', 'b', 'c', 'd', 'g'} '''
    unique = set()
    for string in string_list:
        unique.update(list(string))
    return unique


def sort_char_in_str(string):
    ''' Return a string with characters sorted in alphabetical order:
        'word' -> 'dorw' '''
    char_list = list(string)
    char_list.sort()
    return cat(char_list)


def decode_signal_patterns(code_map):
    '''Find signal pattern for each digit'''
    new_patterns = defaultdict()
    for n in range(10):
        new_signal = [code_map[c] for c in CORRECT_PATTERN[n]]
        new_patterns[sort_char_in_str(new_signal)] = n
    return new_patterns


def decode_output(output_codes, patterns):
    ''' Decode output code using a pattern'''
    output_digits = []
    for code in output_codes:
        output_digits.append(str(patterns[sort_char_in_str(code)]))
    return int(cat(output_digits))


def some_careful_analysis(signal_codes, output_codes):
    # codes with the same number of characters categorized in a dict
    code_length = defaultdict(list)

    p1 = 0
    for code in output_codes:
        if len(code) in [2, 3, 4, 7]: p1 += 1
        code_length[len(code)].append(code)

    for code in signal_codes:
        code_length[len(code)].append(code)

    code_map = defaultdict()

    # solve c | f
    cf = unique_char(code_length[2])

    # solve a
    cfa = unique_char(code_length[3])
    a = cfa.difference(cf)
    code_map['a'] = next(iter(a))

    # solve b | d
    cfbd = unique_char(code_length[4])
    bd = cfbd.difference(cf)

    # solve e | g
    abcdefg = unique_char(code_length[7])
    eg = abcdefg.difference(cf).difference(bd).difference(a)

    # solve c | d | e
    cde = set()
    for code6 in code_length[6]:
        nema = abcdefg.difference(unique_char(code6))
        cde.add(next(iter(nema)))

    # solve remaining letters
    f = cf.difference(cde)
    code_map['f'] = next(iter(f))
    c = cf.difference(f)
    code_map['c'] = next(iter(c))
    b = bd.difference(cde)
    code_map['b'] = next(iter(b))
    d = bd.difference(b)
    code_map['d'] = next(iter(d))
    g = eg.difference(cde)
    code_map['g'] = next(iter(g))
    e = eg.difference(g)
    code_map['e'] = next(iter(e))

    return p1, code_map


CORRECT_PATTERN = {0: 'abcefg',
                   1: 'cf',
                   2: 'acdeg',
                   3: 'acdfg',
                   4: 'bcdf',
                   5: 'abdfg',
                   6: 'abdefg',
                   7: 'acf',
                   8: 'abcdefg',
                   9: 'abcdfg'}


# data = read_input('example08')

data = read_input(8)

p1, p2 = 0, 0
for line in data:

    signal, output = line.split(' | ')
    signal_codes, output_codes = signal.split(' '), output.split(' ')

    p1_line, code_map = some_careful_analysis(signal_codes, output_codes)
    p1 += p1_line

    patterns = decode_signal_patterns(code_map)

    output_value = decode_output(output_codes, patterns)
    p2 += output_value

print(p1)
print(p2)
