#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 8.2 (list subsets)

Make a recursive function subsets(L) that given a list L returns a list of all
subsets of L (each subset being a list). E.g. subsets([1, 2]) should return
[[], [1], [2], [1, 2]]. The order of the returned lists can be arbitrary.

"""


def subsets(L):
    if L == []:
        return [[]]

    x = subsets(L[1:])

    return x + [[L[0]] + y for y in x]


L = [1, 2, 3, 4, 5]
print(subsets(L))


# Hjælp herfra https://stackoverflow.com/questions/26332412/python-recursive-function-to-display-all-subsets-of-given-set
