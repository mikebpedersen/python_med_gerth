#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:57:00 2020

@author: JensTrolle
"""

x = [0, 7]

# Same as in exercise 2, but now original x is a list containing 2 objects.
x[0] = x

# Prints x, which is a list containing inf many lists inside lists and 7.
print(x)

# Prints the 2nd element of x, which is 7.
print(x[1])

# Prints the 1st element of the 2nd element of x, which is 7, and so on.
print(x[0][1])
print(x[0][0][1])
print(x[0][0][0][1])
print(x[0][0][0][0][1])
print(x[0][0][0][0][0][1])
