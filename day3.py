# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-02 22:19:00
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/3
# ===============================

import pandas as pd
raw_data = pd.read_clipboard(sep = ' ',header=None)

# ===============================
# Part 1 & 2
# ===============================

# prepare endless tree area
trees = raw_data[0].apply(lambda x: x * 100).to_list()

def count_tree(tree_list = None ,slopes = None):
    results = []
    for x,y in slopes:
        cnt = 0
        for i in range(0,len(trees)):
            if i*x >= len(trees):
                pass
            else:
                if trees[i*x][i*y] == "#":
                    cnt += 1
        results += [cnt]
    return results

count_tree(tree_list = trees
            ,slopes = [(1,1),(1,3),(1,5),(1,7),(2,1)])