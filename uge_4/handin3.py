#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
a)
Make a function generate_labels(n), that given an integer n returns a list of n
distinct strings, e.g. 'A', 'B', ... or "L1", 'L2' ...

b)
Make a function permute(L), that given a list L, returns a new list containing
a random permutation of the elements in L.

Hint: Construct the new list left-to-right by randomly selecting an element
not selected so far. To generate a random integer in the interval [a,b], you
can you the function randint(a,b) from the module random (use from random
import randint to get access to the function).

Note. Using the function shuffle from the module random to solve the question
would be considered cheating.

c)
Make a function pairs(L), that given a list of comparable elements,
returns a list of all pairs, i.e. tuples with two elements, (a, b) where a < b.

d)
Make a function canonical_triplets(A, B) that returns a list of all canonical
triples where the left subtree contains a label from A and the right subtree
is a pair from B.

e)
Make a function anchored_triplets(L, R) that returns a list of all canonical
triples anchored at a node where the left subtree contains the labels in the
list L and the right subtree contains the labels in the list R.
"""
