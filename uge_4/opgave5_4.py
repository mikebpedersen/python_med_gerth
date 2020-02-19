#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Make a method flatten(L) that given a list of lists L = [L1,L2,...,Lk]
returns one list that is the concatenation of all lists, i.e. L1+L2+···+Lk.
Your implementation should use list comprehension.
"""

L = [[1, 2], [3, 4], [6, 3]]


def flatten(lists):
    return [elm for l in lists for elm in l]


print(flatten(L))

"""
b = []


def flatten2(lists):
    for l in lists:
        for elm in l:
            b.append(elm)
    return b

print(flatten2(lists))
"""
