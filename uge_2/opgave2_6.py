#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 28 12:20:03 2020

@author: JensTrolle
"""

x = int(float(input("Input your natural number here: ")))

while x < 1:
    print("You have to input a natural number, try again.")
    x = int(input("Input a natural number here: "))

n = x
i = 2
numbers = []

# Use append function to add divisors to list.
while x != 1:
    if x % i == 0:
        numbers.append(i)
        x = x // i
    else:
        i += 1

if n == 1:
    numbers.append(1)
    print("1 is not super interesting, as you can always divide by it.")

# https://bit.ly/36DPKUr - stackoverflow article about joining lists.
else:
    divisors = '*'.join(map(str, numbers))
    print("Here are the prime factors of your number: ", n, "=", divisors)
