# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-01 14:04:25
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/1
# ===============================



# ===============================
# Part 1
# ===============================
import pandas as pd


expense = pd.read_clipboard(sep = ' ',header=None)
exp_list = expense.iloc[:,0].tolist()
exp_dedup = list(dict.fromkeys(exp_list))

# method 1: naive loop over
def pair_to_sum(item_list = None, sum_amount = None):
    result = {}
    pair = {}
    temp_list = item_list.copy()
    
    for i in range(0,len(temp_list) ):
        x = temp_list.pop(0)
        result[ x ]  = [x + y  for y in temp_list]
    
    for k,v in result.items():
        if sum_amount in v:
            pair[k*(sum_amount - k)] = [k,sum_amount - k]

    return pair

pair_to_sum(exp_dedup,2020)

# rewrite to simplify:
def pair_to_sum(item_list = None, sum_amount = None):
    result = {}

    for x, A in enumerate(exp_dedup):
        for y, B in enumerate(exp_dedup[x:]):
                if A + B  == sum_amount:
                    result[A*B] = [A,B]
    return  result

pair_to_sum(exp_dedup,2020)

# ===============================
# Part 2
# ===============================

def trio_to_sum(item_list = None, sum_amount = None):
    result = {}

    for x, A in enumerate(exp_dedup):
        for y, B in enumerate(exp_dedup[x:]):
            for z, C in enumerate(exp_dedup[y:]):
                if A + B + C == sum_amount:
                    result[A*B*C] = [A,B,C]
    return  result

trio_to_sum(exp_dedup,2020)

