#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 8.1 (upper and lower cases)

Make a recursive function cases(s) that given a string s, generates a list of
all possible upper and lower case combinations of the letters in the string.
E.g. cases("abcB") should return a list containing the following 16 strings
['abCb', 'abCB', 'abcb', 'abcB', 'aBCb', 'aBCB', 'aBcb', 'aBcB', 'AbCb',
 'AbCB', 'Abcb', 'AbcB', 'ABCb', 'ABCB', 'ABcb', 'ABcB'].

Hint. Use str.lower() and str.upper()to convert a string containing one letter
to lower and upper case.

"""