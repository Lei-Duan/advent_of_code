# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-14 20:58:39
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/14
# ===============================

# ===============================
# Data
# ===============================
import clipboard
import numpy as np
raw = clipboard.paste()  
data = raw.split(sep = '\n')

program = []
for i in data:
    if 'mask' in i:
        program += [ [ 'mask', i.replace('mask = ','')]  ]
    elif 'mem'  in i:
        program += [ ['mem', int( re.search(r'\[(.*?)\]',i).group(1) ), int( i.split('=')[1] ) ] ] 
program[0:10]

# ===============================
# Part 1
# ===============================
def decode(num, length = 36):
    def dec2bin(num):
        l = []
        if num < 0:
            return '-' + dec2bin(abs(num))
        while True:
            num, remainder = divmod(num, 2)
            l.append(str(remainder))
            if num == 0:
                return ''.join(l[::-1])
            
    return '0' * (length - len( dec2bin(num) )) + str(dec2bin(num))

def mask_func(num,mask):
    result = ''
    for n in range(len(mask)):
        if mask[n] == '0':
            result += '0'
        elif mask[n] == '1':
            result += '1' 
        else:
            result += num[n]
    return result

# unit test
num = 0
print(decode(num))
print(mask_func(decode(num) , 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'))
print(int( mask_func(decode(num) , 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X'),2) )

mem  = {}
mask = 'X'*36
for code in program:
    if code[0] == 'mask':
        mask = code[1] 
    else:
        mem[code[1]] = int(mask_func(decode(code[2]) , mask),2)
        
sum([v for k,v in mem.items()])


# ===============================
# Part 2
# ===============================

# unit test
test_data = ['mask = 000000000000000000000000000000X1001X',
'mem[42] = 100',
'mask = 00000000000000000000000000000000X0XX',
'mem[26] = 1']

test_program = []
for i in test_data:
    if 'mask' in i:
        test_program += [ [ 'mask', i.replace('mask = ','')]  ]
    elif 'mem'  in i:
        test_program += [ ['mem', int( re.search(r'\[(.*?)\]',i).group(1) ), int( i.split('=')[1] ) ] ] 
test_program



mem  = {}
mask = '0'*36
for code in program:
    if code[0] == 'mask':
        mask = code[1] 
    else:
        address = mask_func2(decode(code[1]) , mask)
        float_pos = [i for i in range(len(address)) if address.startswith('X', i)]
        for i in range(2**len(float_pos)):
            sub_string = decode(i,length = len(float_pos))
            add = address
            for s,pos in zip(sub_string,float_pos):
                add = add[:pos] + str(s) + add[(pos+1):]
            mem[add] = code[2]
                       
sum([v for k,v in mem.items()])