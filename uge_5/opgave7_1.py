#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 7.1 (average)
"""

"""
Write a function average2(x,y) that computes the average of x and y,
i.e. (x+y)/2.
"""


def average2(x, y):
    return (x+y)/2


print(average2(2, 6))


"""
Write a function list_average(L) that computes the average of the numbers in
the list L.
"""


L = [2, 3, 4, 31]


def list_average(L):
    return sum(L)/len(L)


print(list_average(L))


"""
Write a function average(x1,...,xk) that takes an arbitray number of arguments
(but at least one) and computes the average of x1, ..., xk.

Hint. Use a * to indicate an arbitrary argument list.
"""


def average(x, *y):
    
    return list_average([x]+list(y))


print(average(1))
