#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 12:01:25 2020

@author: JensTrolle
"""

# Makes a list from the range 4 to 8.
print(list(range(4, 9)))

# Same as below.
print(list(range(9, 4, -1)))

# Runs through the range, as 8>3, we have to use -1 to go through it correctly.
print(list(range(8, 3, -1)))

# Reverses the range.
print(list(range(4, 9)[::-1]))
