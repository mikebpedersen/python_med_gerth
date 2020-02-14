#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use list comprehension, enumerate, and sum to evaluate a polynomial given by
its coefficients. E.g. for x = 7 and coefficients (5, 0, -2, 3) your code
should compute the value 936.
"""

x = 7

thing = (5, 0, -2, 3)

print(sum([a * (x**i) for i, a in enumerate(thing)]))
