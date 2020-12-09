# ===============================
# -*- coding: utf-8 -*-
# @Date    : 2020-12-06 23:35:28
# @Author  : lduan
# @Project : https://adventofcode.com/2020/day/7
# ===============================

# ===============================
# Data
# ===============================
import pandas as pd
import clipboard
raw = clipboard.paste()
text = raw.split(sep = '\n')
d = {i:t for i,t in enumerate(text) }

d_clean = {}
for k,v in d.items():
    text = re.split(' bag[s]?[.,]? ?', v)
    text = [t.replace('contain ', '') for t in text]
    text.remove('')
    d_clean[text[0]] = text[1:]

# ===============================
# Part 1
# ===============================
def find_ancestry(d = None,son = None ):
    bags = [] + son
    addition = 1 # for getting into the loop
    while addition > 0:
        addition = 0
        for k,v in d_clean.items():
            for b in bags:
                if b in ''.join(v):
                    if k not in bags:
                        addition += 1
                        bags = bags + [k]

    return bags

len(find_ancestry(d_clean,son = ['shiny gold'])) - 1



# ===============================
# Part 2
# ===============================
def loop_bag(father = None):
    son = {}
    for k,v in d_clean.items():
        for b in father:
            mult = father[b]
            if b == k:
                for i in v:
                    if len(re.findall(r'\d+', i) ) > 0:
                        if re.split('\d+ ', i)[1] not in son:
                            son[ re.split('\d+ ', i)[1] ] = int(re.findall(r'\d+', i)[0])*mult
                        else:
                            son[ re.split('\d+ ', i)[1] ] = son[ re.split('\d+ ', i)[1] ] + int(re.findall(r'\d+', i)[0])*mult

    return son


def find_offspring(start = 'shiny gold',cnt = 1):
    i = 0
    bag_list = {}
    while i <= 10:
        if i == 0:
            bag_list[i] = {start:cnt}
        else:
            if len(loop_bag(bag_list[i-1])) == 0:
                break
            else:
                bag_list[i] = loop_bag(bag_list[i-1])
        i += 1
    return bag_list

bag_list = find_offspring()


def sum_bags(bag_list = None):
    sum_bag = 0
    for k,v in bag_list.items():
        sum_bag += sum(v.values())
    return sum_bag

sum_bags(bag_list) - 1

