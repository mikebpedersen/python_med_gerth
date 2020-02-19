#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint


"""
a)
Make a function generate_labels(n), that given an integer n returns a list of n
distinct strings, e.g. 'A', 'B', ... or "L1", 'L2' ...
"""

x = int(input("Skriv her, hvor mange strenge du vil have: "))

while x <= 0:
    x = int(input("Du skal have over 0 strenge, prøv igen: "))


def generate_labels(n):
    return [("L%s" % (i+1)) for i in range(n)]


print(generate_labels(x))


"""
b)
Make a function permute(L), that given a list L, returns a new list containing
a random permutation of the elements in L.

Hint: Construct the new list left-to-right by randomly selecting an element
not selected so far. To generate a random integer in the interval [a,b], you
can use the function randint(a,b) from the module random (use from random
import randint to get access to the function).

Note. Using the function shuffle from the module random to solve the question
would be considered cheating.
"""


def permute(L):
    new = []
    for i in range(0, len(L))[::-1]:
        b = randint(0, i)
        new.append(L.pop(b))
    return new


print(permute(generate_labels(x)))


"""
c)
Make a function pairs(L), that given a list of comparable elements,
returns a list of all pairs, i.e. tuples with two elements, (a, b) where a < b.
"""


def pairs(L):
    return [(a, b) for a in L for b in L if a < b]


print(pairs(generate_labels(x)))


"""
d)
Make a function canonical_triplets(A, B) that returns a list of all canonical
triples where the left subtree contains a label from A and the right subtree
is a pair from B.
"""


A1 = generate_labels(x)[:(x//2)]
B1 = generate_labels(x)[(x//2):]


def canonical_triplets(A, B):
    return[(i, j) for i in A for j in pairs(B)]


print(canonical_triplets(A1, B1))


"""
e)
Make a function anchored_triplets(L, R) that returns a list of all canonical
triples anchored at a node where the left subtree contains the labels in the
list L and the right subtree contains the labels in the list R.
"""


def anchored_triplets(L, R):
    e = [(a, b) for a in R for b in pairs(L)]
    e.extend(canonical_triplets(L, R))
    return e


print(anchored_triplets(A1, B1))
