# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-14 23:50:04
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/15
# ===============================

# ===============================
# Data
# ===============================
data = [0,6,1,7,2,19,20]

# ===============================
# Part 1 & 2
# ===============================
element = {v:i for i,v in enumerate(data[:-1])}
while True:
    last    = data[-1]
    new_ind = len(data) - 1
    if last in element:
        data += [new_ind - element[last] ]
        element[last] = new_ind    
    else:
        data += [0]
        element[last] = new_ind
#     print(last)
#     print(data)
#     print(element)
    if len(data) == 30000000:
        break

data[-1]