#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Write a method histogram that given a list of elements, returns a list of pairs
(element, frequency). E.g. hist(['A', 'B', 'A', 'A', 'C', 'E', 'C'])
should return [('A', 3), ('B', 1), ('C', 2), ('E', 1)]

HINT: Use a dictionary and the dictionary method get.

Note. In the standard library module collections the
Counter method implements the same functionality:

import collections
hist = list(collections.Counter(['A', 'B', 'A', 'A', 'C', 'E', 'C']).items())
"""

elements = ['A', 'B', 'A', 'A', 'C', 'E', 'C']


def hist(x):
    freq = {}
    for e in elements:
        freq[e] = freq.get(e, 0)+1
    return list(freq.items())


print(hist(elements))
