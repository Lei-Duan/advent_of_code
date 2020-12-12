# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-11 23:33:14
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/12
# ===============================

# ===============================
# Data
# ===============================
import clipboard
import numpy as np
raw = clipboard.paste()  
data = raw.split(sep = '\n')
text = [ [d[0], int(d[1:])]  for d in data ]

# ===============================
# Part 1
# ===============================
dir_map = {'E':[0,1],'W':[0,-1],'N':[1,1],'S':[1,-1],'L':1, 'R':-1}

start = [0, 0, 0]
for action,value in text:
    if action in ['E','W','N','S']:
        # east / north as main axis
        start[ dir_map[action][0] ] += dir_map[action][1] * value
            
    elif action in ['L','R']:
        # east / north as main axis
        start[2] += dir_map[action] * value
    elif action == 'F':
        angle = math.radians(start[2])
        start[0] += value * math.cos(angle)
        start[1] += value * math.sin(angle)

start[0] + start[1]

# ===============================
# Part 2
# ===============================

start = [0,0]
pt    = [10,1]
for action,value in text:
    if action in ['E','W','N','S']:
        # east / north as main axis
        pt[ dir_map[action][0] ] += dir_map[action][1]  * value
        
    elif action in ['L','R']:
        # east / north as main axis
        x,y = pt
        lenth = math.hypot(x,y)
        angle = math.degrees( math.atan2(y,x)) + dir_map[action] * value
        pt[0] = lenth * math.cos(math.radians(angle))
        pt[1] = lenth * math.sin(math.radians(angle))
        
    elif action == 'F':
        start[0] += value * pt[0]
        start[1] += value * pt[1]

start[0] + start[1]