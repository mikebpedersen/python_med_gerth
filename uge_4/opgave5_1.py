#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Use list comprehension, enumerate, and sum to evaluate a polynomial given by
its coefficients. E.g. for x = 7 and coefficients (5, 0, -2, 3) your code
should compute the value 936.
"""

n = int(input("Input what length your polynomial is: "))

while n <= 0:
    n = int(input("Your polynomial cannot be of size lower than 1: "))

x = int(input("Input the integer you want your polynomial evaluated at: "))

coef = []

[coef.append(int(input("Input your coefficient here: "))) for i in range(n)]

print(sum([a * (x**i) for (i, a) in enumerate(coef)]))
