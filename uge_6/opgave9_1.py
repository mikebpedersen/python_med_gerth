#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 9.1 (bitonic minimum)

We call a list L=[x1, ..., xn] bitonic, if there exists a k, 1<k<n, such that
x1 > x2 > ··· > xk-1 > xk < xk+1 < ··· < xn, i.e. xk is the minimum of the
list. Write a method bitonic_min that given a list, returns the minimum of the
list. Your implementation should use binary search (i.e. you cannot use the
Python builtin min function).

Example: bitonic_min([10,7,4,2,3,5,9,11]) should return 2.

"""
