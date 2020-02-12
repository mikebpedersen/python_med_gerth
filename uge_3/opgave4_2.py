#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 11:52:06 2020

@author: JensTrolle
"""

# a is a list containing the integer 42
a = [42]

# 1st element of a is defined to be the entire list of a, meaning that the
# 1st element of a is the entire list of a, which is set equal to the entire
# list of a - and so on.
a[0] = a

print(a)
