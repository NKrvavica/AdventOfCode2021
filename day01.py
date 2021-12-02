# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:53:59 2021

@author: Nino
"""

import numpy as np
import pandas as pd

fname = './Day01/day01.txt'

depths = np.loadtxt(fname)

# part 1
diff = np.diff(depths)
increases = diff[diff > 0]
print(f'Solution to part one: {increases.size}')

# part 2
depths_s = pd.Series(depths)
rolling_sum = depths_s.rolling(3, center=True).sum()
rolling_diff = rolling_sum.diff()
rolling_inc = rolling_diff.loc[rolling_diff > 0]
print(f'Solution to part two: {rolling_inc.size}')
