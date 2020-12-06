# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-06 00:22:05
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/6
# ===============================

# ===============================
# Data
# ===============================

import pandas as pd
import clipboard

raw = clipboard.paste()  
text = raw.split(sep = '\n\n')
d = { i:t.split('\n') for i,t in enumerate(text) }

# ===============================
# Part 1
# ===============================


def unique_str_cnt(text):
    return len(set(text))

result = 0
for k,v in d.items():

    result += unique_str_cnt (''.join(v) )

result



# ===============================
# Part 2
# ===============================

result = 0
for k,v in d.items():
    ppl = len(v)
    for letter in set( ''.join(v) ):
        letter_cnt = ''.join(v).count(letter)
        if letter_cnt == ppl:
            result += 1
result