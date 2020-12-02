# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-01 21:36:54
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/2
# ===============================

import pandas as pd
raw_data = pd.read_clipboard(sep = ' ',header=None)

# ===============================
# Part 1
# ===============================
def pwd_checker(raw_df = None):
    # data clean
    df = raw_df[0].str.split("-", n =1, expand = True).rename(columns = {0:'min_ct',1:'max_ct'})
    df['letter'] = raw_df[1].str.strip(":")
    df['pwd'] = raw_df[2]
    df = df.astype({'min_ct':int,'max_ct':int}) 

    # validate
    df['letter_ct']    = df.apply(lambda x: x.pwd.count(x.letter) , axis=1)
    df['validate'] = df.apply(lambda x: (x.letter_ct >= x.min_ct) & (x.letter_ct <= x.max_ct)  , axis=1)
    return df['validate'].sum()

pwd_checker(raw_data)



# ===============================
# Part 2
# ===============================
def pwd_checker_2(raw_df = None):
    # data clean
    df = raw_df[0].str.split("-", n =1, expand = True).rename(columns = {0:'pos_1',1:'pos_2'})
    df['letter'] = raw_df[1].str.strip(":")
    df['pwd'] = raw_df[2]
    df = df.astype({'pos_1':int,'pos_2':int}) 

    # validate
    df['validate'] = df.apply(lambda x: True if (x.pwd[x.pos_1-1] + x.pwd[x.pos_2-1]).count(x.letter) == 1 else False , axis=1)
    return df['validate'].sum()
    
pwd_checker_2(raw_data)

