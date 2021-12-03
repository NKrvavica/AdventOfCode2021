# -*- coding: utf-8 -*-
"""
Created on Fri Dec  3 07:56:15 2021

@author: Nino
"""

from aoc import *
import numpy as np
import pandas as pd


def bin_array_to_dec(a):
    return int(cat(map(str, a)), 2)


def part1(data_array):
    # gamma rate
    common_bits = data_array.median(axis=0).values.astype(int)
    gamma_rate = bin_array_to_dec(common_bits)

    # epsilon rate
    least_common_bits = 1 - common_bits
    epsilon_rate = bin_array_to_dec(least_common_bits)

    return gamma_rate * epsilon_rate


def part2(data_array):
    # OXygen generator
    idx = 0
    keep = data_array
    while keep.index.size > 1:
        bit =  keep[idx].median(axis=0)
        keep = keep.loc[keep[idx] == np.ceil(bit).astype(int)]
        idx += 1
    oxy_gen_rating = bin_array_to_dec(keep.values[0])

    # CO2 scrubber
    idx = 0
    keep = data_array
    while keep.index.size > 1:
        bit =  1 - keep[idx].median(axis=0)
        keep = keep.loc[keep[idx] == np.floor(bit).astype(int)]
        idx += 1
    co2_scrubb_rating = bin_array_to_dec(keep.values[0])

    return oxy_gen_rating * co2_scrubb_rating


data = read_input(3)
data_array = pd.DataFrame(mapl(digits, data))

print(part1(data_array))
print(part2(data_array))
