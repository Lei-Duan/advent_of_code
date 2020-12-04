# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-03 23:05:26
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/4
# ===============================

import pandas as pd
import re

with open('./day4.txt') as f:
    lines = f.read()

# ===============================
# Part 1 & 2
# ===============================

# data clean
text = lines.replace('"','').split('\n\n')
text_cl = [i.replace("\n"," ") for i in text ]

# list to dict
d = {i:text_cl[i] for i in range(0,len(text_cl))}

# change deep level data into dict as well
## loop
dicts = {}
for k,v in d.items():
    y = {}
    for t in v.split(' '):
        x = t.split(':')
        y[x[0]] = x[1]
    dicts[k] = y
## alternative dict comprehension
# dicts = {k:{i.split(":")[0]:i.split(":")[1] for i in v.split(' ')}  for k,v in d.items() }


def validate_checker(my_dict = None):
    result = 0
    for k,v in my_dict.items():
        if ('byr' in v.keys() ):     
            if (1920 <=  int(v['byr']) <= 2002 ):
                    if 'iyr' in v.keys():
                        if (2010 <=  int(v['iyr']) <= 2020 ):
                            if 'eyr' in v.keys():
                                if (2020 <=  int(v['eyr']) <= 2030 ):
                                    if 'hgt' in v.keys():
                                        if 'cm' in v['hgt']:
                                            if 150 <= int(v['hgt'].replace('cm', '')) <= 193:
                                                if 'hcl' in v.keys():
                                                    if bool(re.search( '^#[0-9a-f]{6}$',v['hcl'])):
                                                        if 'ecl' in v.keys():
                                                            if v['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                                                                if 'pid' in v.keys():
                                                                    if bool(re.search( '^[0-9]{9}$',v['pid'])):
                                                                        result += 1
                                        elif 'in' in v['hgt']:
                                            if  59 <= int(v['hgt'].replace('in', '')) <= 76:
                                                if 'hcl' in v.keys():
                                                    if bool(re.search( '^#[0-9a-f]{6}$',v['hcl'])):
                                                        if 'ecl' in v.keys():
                                                            if v['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                                                                if 'pid' in v.keys():
                                                                    if bool(re.search( '^[0-9]{9}$',v['pid'])):
                                                                        result += 1
    return result


validate_checker(dicts)