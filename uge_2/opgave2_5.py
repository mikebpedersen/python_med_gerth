#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:19:50 2020

@author: JensTrolle
"""
x = int(input("Input an x greater than or equal to 2: "))
i = 2

while x < 2:
    print("Try again - your x has to be greater than or equal to 2.")
    x = int(input("Input an x greater than or equal to 2: "))

"""
We check for primality with the followung while loop. If we have looped far
enough to have i == x, then the number has to be prime and we break. If x mod
i is 0, then x is not prime, and we break. If none of these conditions hold
we add 1 to i, unill one is satisfied.
"""

while True:
    if i == x:
        print("Your number is prime, congratulations!")
        break
    elif x % i == 0:
        print("Your number is not prime, as it is divisible by % i" % (i))
        break
    else:
        i += 1
