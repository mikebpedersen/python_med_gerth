#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 15:20:46 2020

@author: JensTrolle
"""

from math import pi
print("A string: '%s'" % "Hello World")
# prints the string and inserts "Hello World" as a string inside ''.

print("An integer: %s" % 27)
# prints the string and inserts 27 as a string.

print("A float: %s" % 27.0)
# prints the string and inserts 27.0 as a string.

print("A float: %s" % pi)
# prints the string and inserts pi as a string.

print("A float: %s " % pi*2)
# prints the string twice and inserts pi as a string.

print("A float: %s " % (pi*2))
# prints the string and inserts (2 times pi) as a string.

print("A float: %.2f " % pi)
# prints the string and inserts pi as a float with 2 decimals.

print("A float: [%5.2f] " % pi)
# prints the string, inserts pi to 2 decimal places
# and reserves a length of 5 characters.

print("A float: [%+6.2f] " % pi)
# prints the string, inserts pi to 2 decimal places and adds a + sign, in front
# of pi, and reserves the last space.

print("A float: [%+.2f] " % pi)
# prints the string, inserts pi to 2 decimal places and adds a + sign.

print("A float: [%08.2f] " % pi)
# prints the string, inserts pi to 2 decimal places and adds 0's where
# there is space in the reserved 8 chars.

print("An integer: [%08d] " % 42)
# prints the string and inserts 0's until a length of 8 has been reached.
