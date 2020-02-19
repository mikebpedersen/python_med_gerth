#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
HANDIN 3: Triplet Distance (Part 1)


Afleveringen er lavet af:
    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflektion:

'''

# Opgave a)

# Input af mængde af strenge
x = int(input("Skriv her, hvor mange strenge du vil have: "))

# Tjek for mængde større end 0
while x <= 0:
    x = int(input("Du skal have over 0 strenge, prøv igen: "))


# Definerer funktion der giver liste med labels vha. list comprehention.
# Her er det vigtigt at pointere, at måden vi har definereret
# generate_labels(n) på gør, at vi kan sammenligne elementerne,
# f.eks. er 'L1' < 'L2'.
def generate_labels(n):
    return [("L%s" % (i+1)) for i in range(n)]


# Printer listen af x labels vha. generate_labels(n)
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

from random import randint


# Definerer funktionen permute(L), der permuterer en given liste. 
# Vi gør dette på den måde der er beskrevet i hintet i opgavebeskrivelsen,
# ved at starte med hele L, og så tage et tilfældigt element ud, putte det ind
# i en ny liste. Derefter fjerner vi et element fra L og begynder igen, indtil
# L er tom.
def permute(L):
    new = []
    for i in range(0, len(L))[::-1]:
        b = randint(0, i)
        new.append(L.pop(b))
    return new

# Printer en permutation af x labels, ved at bruge permute(generate_labels(n)).
print(permute(generate_labels(x)))


"""
c)
Make a function pairs(L), that given a list of comparable elements,
returns a list of all pairs, i.e. tuples with two elements, (a, b) where a < b.
"""


# Definerer funktionen pairs(L), der returnerer (a, b) for elementet a i L,
# hvis der for b i L gælder, at a < b. Vi sorterer også elementerne for at
# tage højde for, at vi f.eks. har 'L1' < 'L10' < 'L11' < 'L2'.
def pairs(L):
    return sorted([(a, b) for a in L for b in L if a < b])


# Printer parene der er i generate_labels(n).
print(pairs(generate_labels(x)))


"""
d)
Make a function canonical_triplets(A, B) that returns a list of all canonical
triples where the left subtree contains a label from A and the right subtree
is a pair from B.
"""

# Vi splitter vores liste af labels (generate_labels(x)) op i to lister. Hvis
# x er ulige har 
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
    e = canonical_triplets(L, R)
    f = canonical_triplets(R, L)
    e.extend(f)
    return e


print(len(anchored_triplets(A1, B1)))
