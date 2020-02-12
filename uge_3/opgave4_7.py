#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 10:25:33 2020

@author: JensTrolle
"""

# x = int(input("Skriv her hvor mange intervaller du vil finde den disjunkte foreningsmængde af: "))
total_list = sorted([[1, 3], [6, 10], [2, 5], [8, 13]])
"""
total_list = []
for i in range(1, x+1):
    inside_list = list((int(input("Skriv her dit første tal i intervallet: ")),
                        int(input("Skriv her dit andet tal i intervallet: "))))
    sorted(inside_list)
    total_list.append(inside_list)
"""
sort_inputs = sorted(total_list)
print(sort_inputs)

final_list = []
last_spot = sort_inputs[0][1]
first_min = sort_inputs[0][0]

for i in range(0, len(sort_inputs)):
    if last_spot < sort_inputs[i][0]:
        interval = [first_min, sort_inputs[i][1]]
        final_list.append(interval)
        first_min = sort_inputs[i][0]
    last_spot = sort_inputs[i][1]

print(final_list)
"""
L = [[1, 3], [6, 10], [2, 5], [8, 13]]
L_max = max(L_S)[-1]
for i in range(1, len(L_S)):
    L_high.append(L_S[i][0])
    L_low.append(L_S[i-1][len(L_S[i])-1])
    if max(L_low) < min(L_high):
        L_.append(min(L_low))
        L_.append(max(L_low))
        L_.append(min(L_high))
    L_high = []
    L_low = []
L_.append(L_max)
print(L_)
"""
