#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 22 13:53:55 2020

@author: JensTrolle
"""

k = 0
k = int(input("Skriv her hvor mange tal du vil summere: "))

a = 0
while k > 0:
    a += int(input("Skriv dit tal her: "))
    k = k - 1

print("Her er summen af dine tal: ", a)


"""
        FUVE's løsning:
s = 0
for i in range(k):
    s+= int(input("Skriv dit tal her: "))
print("Her er summen af dine tal: ", s)


        Rav's løsning:
print("Her er summen af dine tal: ", sum(int(input("Skriv dit tal her: "))
for i in range(int(input("Skriv her hvor mange tal du vil summere: ")))))
"""
