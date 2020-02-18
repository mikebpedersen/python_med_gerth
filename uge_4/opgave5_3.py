#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement your own version my_zip of zip,
such that my_zip([L1,L2,...,Lk]) == list(zip(L1,L2,...,Lk)).
"""

first = ['Donald', 'Mickey', 'Scrooge']
last = ['Duck', 'Mouse', 'McDuck']

combined = [first, last]


def my_zip(l):
    n = min([len(x) for x in l])
    L = len(l)
    return [tuple(l[i][j] for i in range(L)) for j in range(n)]

print(my_zip(combined))
