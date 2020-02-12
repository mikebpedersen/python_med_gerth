#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 08:33:16 2020

@author: JensTrolle
"""

import random

while True:
    x, y, z, i, j, k = [random.randint(-100, 100) for _ in range(6)]

    if z == 0 or k == 0:  # skip illegal input
        continue

    r = range(x, y, z)[i:j:k]

# Indsæt kode efter dette:

    print("range(%s,%s,%s)[%s:%s:%s] =" % (x, y, z, i, j, k), r)

#    if r != range(a, b, c):
#       print("Wrong range: a b c =", a, b, c)
#      break
