#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Implement your own version my_zip of zip,
such that my_zip([L1,L2,...,Lk]) == list(zip(L1,L2,...,Lk)).
"""

first = ['Donald', 'Mickey', 'Scrooge']
last = ['Duck', 'Mouse', 'McDuck']


def my_zip(x, y):
    return [(x[i], y[i]) for i in range(len(first))]


x = first
y = last

if list(zip(x, y)) == my_zip(x, y):
    print("Det virker!")
