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


"""
Opgave a) - generate_labels(n)
"""

# Input af mængde af strenge
x = int(input("Skriv her, hvor mange strenge du vil have: "))

# Tjek for mængde større end 0
while x <= 0:
    x = int(input("Du skal have over 0 strenge, prøv igen: "))


# Definerer funktion der giver liste med labels vha. list comprehension.
# Her er det vigtigt at pointere, at måden vi har definereret
# generate_labels(n) på gør, at vi kan sammenligne elementerne,
# f.eks. er 'L1' < 'L2'.
def generate_labels(n):
    return [("L%s" % (i+1)) for i in range(n)]


# Printer listen af x labels vha. generate_labels(n)
print(generate_labels(x))


"""
Opgave b) - permute(L)
"""

from random import randint


# Definerer funktionen permute(L), der permuterer en given liste.
# Vi gør dette på den måde der er beskrevet i hintet i opgavebeskrivelsen,
# ved at starte med hele L, og så tage et tilfældigt element ud, putte det ind
# i en ny liste. Derefter fjerner vi et element fra L og begynder igen, indtil
# vi har brugt alle elementer i L.
def permute(L):
    new = []
    for i in range(0, len(L))[::-1]:
        b = randint(0, i)
        new.append(L.pop(b))
    return new


# Printer en permutation af x labels, ved at bruge permute(generate_labels(n)).
print(permute(generate_labels(x)))


"""
Opgave c) - pairs(L)
"""


# Definerer funktionen pairs(L), der returnerer (a, b) for elementet a i L,
# hvis der for b i L gælder, at a < b. Vi sorterer også elementerne for at
# tage højde for, at vi f.eks. har 'L1' < 'L10' < 'L11' < 'L2'.
def pairs(L):
    return sorted([(a, b) for a in L for b in L if a < b])


# Printer parene der er i generate_labels(n).
print(pairs(generate_labels(x)))

"""
Opgave d) - canonical_triplets(A, B)
"""
# Vi splitter vores liste af labels (generate_labels(x)) op i to lister. Hvis
# x er ulige er: len(A1) = len(B1) - 1. Vi gør dette, for at gøre det lettere
# at tjekke resultater i d) og e). Dette er ikke strengt nødvendigt for
# selve opgaven.
A1 = generate_labels(x)[:(x//2)]
B1 = generate_labels(x)[(x//2):]


# Vi definerer funktionen canonical_triplets(A, B), som finder alle canonical
# triplets for A og B. Vi bruger list comprehension og vores funktion pairs(L).
# Vi returnerer tuplen (i, j) for element i i A for hvert element j i pairs(B).
def canonical_triplets(A, B):
    return[(i, j) for i in A for j in pairs(B)]


# Vi printer canonical triplets for listerne A1 og B1.
print(canonical_triplets(A1, B1))


"""
Opgave e) - anchored_triplets(L, R)
"""


# Vi definerer anchored_triplets(L, R) som finder alle canonical triplets,
# der er anchored til en node, hvor det venstre subtree indeholder alle labels
# i listen L og tilsvarende for det højre subtree. Vi anvender funktionen
# canonical_triplets(A, B) fra opgave d), og tilføjer alle canonical triplets
# der bliver lavet, hvis man bytter om på A og B.
def anchored_triplets(L, R):
    e = canonical_triplets(L, R)
    f = canonical_triplets(R, L)
    e.extend(f)
    return e


# Vi printer alle anchored triplets for A1 og B1.
print(anchored_triplets(A1, B1))
