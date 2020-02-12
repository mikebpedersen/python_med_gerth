#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:48:02 2020

@author: JensTrolle
"""

a = [[1, 2], [3, 4]]

# b defined as a
b = a

# c defined as a copy of a
c = a[:]

# 1st element of b defined to be [5, 6]
b[0] = [5, 6]

# 1st element of the 1st element of c is defined to be 7
c[1][1] = 7
print(a, b, c)
