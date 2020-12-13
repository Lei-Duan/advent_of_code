# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-12 21:23:04
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/13
# ===============================

# ===============================
# Data
# ===============================
import clipboard
import numpy as np
raw = clipboard.paste()  
data = raw.split(sep = '\n')

# ===============================
# Part 1
# ===============================
schedule = {'time':int(data[0]), 'bus':[int(id) for id in data[1].split(',') if id != 'x'] }
schedule['wait_time'] = [(id - (schedule['time'] % id) ) for id in schedule['bus'] ] 

min_wait_time = min(schedule['wait_time'])
the_bus       = [i for i,w in enumerate(schedule['wait_time']) if w == min_wait_time ]

print( schedule['bus'][the_bus[0]] * min_wait_time )

# ===============================
# Part 2
# ===============================

bus = [i for i in  data[1].split(',')]
new = {int(id):int(diff) for diff,id in enumerate(bus) if id != 'x'}


for t in [bus[0]*n for n in range(1,10000000)]:
for diff,id in enumerate(bus):
    time = t
    if id = 'x':
        time += 1
    elif (time + diff) / id == 0:
        time += 1
    else:
        pass
