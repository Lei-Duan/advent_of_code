# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-10 02:00:38
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/10
# ===============================

# ===============================
# Data
# ===============================
import clipboard
raw = clipboard.paste()  
text = raw.split(sep = '\n')
nums = [int(t) for t in text]
nums.sort()

# ===============================
# Part 1
# ===============================
volt = 0
diff = {1:0,2:0,3:0}
while len(nums) > 0:
    for d in diff:
        if (volt + d) in nums:
            nums.remove(volt + d)
            diff[d] += 1
            volt    += d
            break      
diff[3] += 1 # last chain
diff

# ===============================
# Part 2
# ===============================

# recursive function
cache = {}
def findstep(n) :
    if n in cache:
        return cache[n]  # cache result to help recursive function to run
    elif n not in data + [0]:
        return 0
    elif n in (0,1,2): 
        cache[n] = n
        return n
    else:
        cache[n] = findstep(n - 3) + findstep(n - 2) + findstep(n - 1)  
        return findstep(n - 3) + findstep(n - 2) + findstep(n - 1)  
        
findStep(159)

# dynamic programming
def findstep(n):
    memo[0], memo[1],memo[2] = 0, 1, 2
    for i in range(3, n+1):
        if i not in data:
            memo[i] = memo[i-1] + memo[i-2]
    return memo[n]

findStep(159)