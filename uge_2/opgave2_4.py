#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:19:42 2020

@author: JensTrolle
"""

"""
x = int(input("x: "))

low = 0
high = x + 1

while True:  # low <= sqrt(x) < high
    if low + 1 == high:
        break

    mid = (high + low) // 2

    if mid * mid <= x:
        low = mid
        continue

    high = mid

print(low)  # low = floor(sqrt(x))


First we input an integer.
Then we define low = 0 and high = x + 1 ( our integer + 1 ).
Then we start a while loop.
if low + 1 is equal to high (so our integer is 0), then we break and print 0.
We define mid to be our integer + 1, divided by 2, as low = 0.
if we have mid^2 less than equal x, then we set low equal to mid and continue
to set high = mid.
Then we go back to the begining, and check if low + 1 equals high.
At the end we print the value of low.


"""

x = int(input("x: "))

low = 0
high = x + 1

# Change while statement, to check for later if statement.

while low + 1 < high:

    mid = (high + low) // 2

    if mid * mid <= x:
        low = mid
        # continue changed to setting high = mid.
    else:
        high = mid

print(low)  # low = floor(sqrt(x))


"""
x = int(input("x: "))

print(int(x ** 0.5))  # low = floor(sqrt(x))
"""
