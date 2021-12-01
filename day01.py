# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 07:53:59 2021

@author: Nino
"""

import numpy as np
import pandas as pd

fname = './Day01/day01input.txt'

depths = np.loadtxt(fname)

# part 1
diff = np.diff(depths)
increases = diff[diff > 0]
print(increases.size)

# part 2
depths_s = pd.Series(depths)
rolling_sum = depths_s.rolling(3).sum()
rolling_diff = rolling_sum.diff()
rolling_inc = rolling_diff.loc[rolling_diff > 0]
print(rolling_inc.size)
