#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 7.2 (sum of squares)
"""

"""
Make a function that can take any number of arguments, and returns the sum of
the squares of the values, i.e. square_sum(x1,x2,x3) returns x1**2 + x2**2 +
x3**2.
"""


def square_sum(*x):
    return sum(a**2 for a in [*x])


print(square_sum(1, 2, 3, 4))

"""
Given a list L, e.g. L = [1,2,3,4], use your square_sum function to compute
the sum of squares of the values in L:

Hint. Use a * to indicate an arbitrary argument list.
"""


L = [1, 2, 3, 4]

print(square_sum(*L))
