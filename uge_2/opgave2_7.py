#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:20:09 2020

@author: JensTrolle
"""
"""
import math

n = float(input("Write a number equal to or above 1 here "
                "to approximate the square root: "))
while n <= 1:                               # Check for
    n = float(input("Your number has to be equal to or "
                    "above 1, try again: "))

print("This is the actual square root of", n, ": ", math.sqrt(n))

x = n
# Set limit for how close the approximation has to be.
low = 10e-14

# No need for absolute value, as is squared, and x set = to n.
# If fraction of f(x) over f'(x) is greater than limit, then we
# have reached the precision we want.


# Simple calculation using newtons method as a base.
while low < (( x / 2 ) - ( n / ( 2 * x ))):
    print("Current approximation: ", x)
    x = x - (( x / 2 ) - ( n / ( 2 * x )))

print("This is the approximation of the square root of ", n, ": ", x)
"""

import math

n = float(input("Write a number equal to or above 1 here "
                "to approximate the square root: "))
while n <= 1:                               # Check for input higher than 1.
    n = float(input("Your number has to be equal to or "
                    "above 1, try again: "))

print("This is the actual square root of", n, ": ", math.sqrt(n))

x = n
high = n + 1

# Simple calculation using newtons method.
while high > x:
    print("Current approximation: ", x)
    high = x
    x = x - ((x/2) - (n/(2*x)))

print("This is the approximation of the square root of ", n, ": ", x)
