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


def oxy_generator(numbers, idx):
    return np.ceil(numbers[idx].median(axis=0)).astype(int)


def co2_scrubber(numbers, idx):
    return np.floor(1 - numbers[idx].median(axis=0)).astype(int)


def diagnostic(data_array, method):
    idx = 0
    keep = data_array
    while keep.index.size > 1:
        bit =  method(keep, idx)
        keep = keep.loc[keep[idx] == bit]
        idx += 1
    return bin_array_to_dec(keep.values[0])


def part2(data_array):
    oxy_gen_rating = diagnostic(data_array, oxy_generator)
    co2_scrubb_rating = diagnostic(data_array, co2_scrubber)
    return oxy_gen_rating * co2_scrubb_rating


data = read_input(3)
data_array = pd.DataFrame(mapl(digits, data))

print(part1(data_array))
print(part2(data_array))
