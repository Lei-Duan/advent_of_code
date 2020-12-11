# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-11 03:13:32
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/11
# ===============================

# ===============================
# Data
# ===============================
import clipboard
import numpy as np
raw = clipboard.paste()  
data = raw.split(sep = '\n')
arr = np.array([[ j for j in i] for i in data])    

# ===============================
# Part 1
# ===============================

def adjacent_check(i,j, data = None):
    square = [['L','L','L'],['L','','L'],['L','L','L']] 
    for a,x in zip([i-1,i,i+1],[0,1,2]):
        for b,y in zip([j-1, j , j+1],[0,1,2]):
            if (a == i) & (b == j):
                continue 
            if (a in range(len(data)) ) & (b in range(len(data[0]))):
                square[x][y] = data[a][b]
            else:
                square[x][y] = 'L'
    status = data[i][j]
    cnt  = ''.join([''.join(s) for s in square] ).count('#')
    if (status == 'L') & (cnt == 0):
        choice = '#'
    elif (status == '#') & (cnt >= 4):
        choice = 'L'
    else:
        choice = status
    return choice
    

def run(data, check_func = None):
    end   = copy.deepcopy(arr)
    while True:
        start = copy.deepcopy(end)
        change_seat = 0
        for i in range(len(start)):
            for j in range(len(start[0])):
                end[i][j] = check_func(i,j, data = start)
                if start[i][j] != end[i][j]:
                    change_seat += 1
        if change_seat == 0:
            break
    return ''.join([''.join(s) for s in end ] ).count('#')
        
run(arr,adjacent_check)


# ===============================
# Part 2
# ===============================
def visual_check(i,j,data):
    result = ''
    for x_sign,y_sign in [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]:
        for dist in range(1, min(data.shape) ):
            x = i + x_sign * dist
            y = j + y_sign * dist
            if (x in range(len(data)) ) & (y in range(len(data[0]))):
                if data[x][y] in (['L','#']):
                    result += data[x][y]
                    break
                else:
                    continue
            else:
                result += 'L'
                break
    
    status = data[i,j]
    cnt  = result.count('#')
    if (status == 'L') & (cnt == 0):
        choice = '#'
    elif (status == '#') & (cnt >= 5):
        choice = 'L'
    else:
        choice = status
    return choice

run(arr,visual_check)