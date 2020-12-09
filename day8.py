# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-07 23:38:13
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/8
# ===============================

# ===============================
# Data
# ===============================
import pandas as pd
import clipboard
raw = clipboard.paste()
text = raw.split(sep = '\n')
d = {i:t.split(sep = ' ') for i,t in enumerate(text) }
for k,v in d.items():
    d[k] = [ v[0],v[1][0],int(v[1][1:]) ]       

# ===============================
# Part 1
# ===============================

pointer = 0
pointer_hist = []
accumulator = 0

while pointer not in pointer_hist:
    pointer_hist += [pointer]
    command = d[pointer]
    if command[0] == 'jmp':
        if command[1] == '+':
            pointer += command[2]
        elif command[1] == '-':
            pointer -= command[2]
    elif command[0] == 'acc':
        pointer += 1
        if command[1] == '+':
            accumulator += command[2]
        elif command[1] == '-':
            accumulator -= command[2] 
    elif command[0] == 'nop':
        pointer += 1

accumulator


# ===============================
# Part 2
# ===============================
def operate_checker(d):
    pointer = 0
    pointer_hist = []
    accumulator = 0
    while pointer not in pointer_hist:
        if pointer == len(d):
            print('the code terminates! and the final accumulator is {}'.format(accumulator))
            return('good code')
            break
        else:
            pointer_hist += [pointer]
            command = d[pointer]
            if command[0] == 'jmp':
                if command[1] == '+':
                    pointer += command[2]
                elif command[1] == '-':
                    pointer -= command[2]
            elif command[0] == 'acc':
                pointer += 1
                if command[1] == '+':
                    accumulator += command[2]
                elif command[1] == '-':
                    accumulator -= command[2] 
            elif command[0] == 'nop':
                pointer += 1
                
    if pointer < len(d):
        print('It runs into an infinite loop and the loop starts at ' + str(pointer_hist[-1]))
        return('bad code')


import copy

c = 0
while c <= len(d):
    d_altered = copy.deepcopy(d)
    if d_altered[c][0] in ('jmp','nop'):
        if d_altered[c][0] == 'jmp':
            d_altered[c][0] = 'nop'
        elif d_altered[c][0] == 'nop':
            d_altered[c][0] = 'jmp'
        if operate_checker(d_altered) == 'good code':
            break
        else:
            c += 1
        
    else:
        c += 1