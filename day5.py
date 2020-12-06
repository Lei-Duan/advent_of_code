# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-06 00:16:41
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/5
# ===============================

import pandas as pd
import numpy as np
raw_data = pd.read_clipboard(sep = '/n',header=None)

# ===============================
# Part 1 & 2
# ===============================

d = dict(raw_data[0])

def cut_half(ranges, t= 'F'):
    half = ( ranges[1] - ranges[0]) / 2
    if t in ('F','L'): 
        ranges[1] = np.floor(ranges[1] - half)
    elif t in ("B",'R'):
        ranges[0] = np.ceil(ranges[0] + half)
    return ranges


result = pd.DataFrame()
for k,v in d.items():
    row_range = [0,127]
    col_range = [0,8]
    for rows in v[0:7]:
        cut_half(row_range, t = rows)
    for cols in v[7:10]:
        cut_half(col_range, t = cols)
    result[0:2] = [row_range[0],col_range[0],row_range[0]*8+col_range[0]] 

result