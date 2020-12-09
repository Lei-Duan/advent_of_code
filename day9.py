# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-09 01:54:12
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/9
# ===============================

# ===============================
# Data
# ===============================
import clipboard
raw = clipboard.paste()  
text = raw.split(sep = '\n')
nums = [int(t) for t in text]

# ===============================
# Part 1
# ===============================
def XMAS_checker(num_list = None):
    result = 'invalid'
    for i in num_list[:-1]:
        if ( (num_list[-1] - i) in num_list[:-1] ) & (i*2 != num_list[-1] ):
            result = 'valid'
            break
    return result

result = []
for i,n in enumerate(nums):
    if i <= 24:
        result += ['valid']
    else:
        result += [XMAS_checker(nums[i-25:i+1])]
result

first_exception = [i for i,r in enumerate(result) if r == 'invalid'][0]
nums[first_exception]

# ===============================
# Part 2
# ===============================
target = 15690279
for set in range(2,50):
    for i in range(len(nums)):
        if sum(nums[i:i+set]) == target:
            print(min(nums[i:i+set]))
            print(max(nums[i:i+set]))
            print( min(nums[i:i+set]) + max(nums[i:i+set]) )
            break