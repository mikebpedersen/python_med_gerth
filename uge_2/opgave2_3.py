#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 17:00:07 2020

@author: JensTrolle
"""

a = int(input("Input 1: "))
b = int(input("Input 2: "))
c = int(input("Input 3: "))
d = int(input("Input 4: "))

e = min(a, b)
f = max(a, b)
g = min(c, d)
h = max(c, d)

i = min(f, h)
j = max(e, g)

if f < g or h < e:
    print("The intervals", [e, f], "and", [g, h], "don't overlap.")
else:
    print("The intervals", [e, f], "and", [g, h], "overlap in the interval:",
          [min(i, j), max(i, j)])
