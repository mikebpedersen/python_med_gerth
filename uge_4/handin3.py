#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
HANDIN 3: Triplet Distance (Part 1)


Afleveringen er lavet af:
    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflektion:
Oprindeligt havde vi lavet de fleste af opgaverne uden list comprehension,
men ved at gå logisk gennem vores for-loops fik vi defineret vores funktioner
vha. list comprehensions. F.eks. havde vi en smule svært ved at lave opgave b)
med list comprehension, og havde defineret en tom liste, som vi appendede
et tilfældigt element fra L til, men ved at bruge list comprehension, behøvede
vi ikke at definere den tomme liste.
'''


# Vi importerer randint fra random for at kunne generere tilfældige tal i
# opgave b).
from random import randint


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
print(("\nHer er en liste af % s unikke labels: \n" % x), generate_labels(x),
      "\n")


"""
Opgave b) - permute(L)
"""

# Definerer funktionen permute(L), der permuterer en given liste.
# Vi gør dette på den måde der er beskrevet i hintet i opgavebeskrivelsen,
# ved at starte med hele L, og så tage et tilfældigt element ud, putte det ind
# i en ny liste. Derefter fjerner vi et element fra L og begynder igen, indtil
# vi har brugt alle elementer i L.


def permute(L):
    return [L.pop(randint(0, i)) for i in range(0, len(L))[::-1]]


# Printer en permutation af x labels, ved at bruge permute(generate_labels(n)).
print(("Her er en tilfældig permutation af de % s labels: \n" % x),
      permute(generate_labels(x)), "\n")


"""
Opgave c) - pairs(L)
"""


# Definerer funktionen pairs(L), der returnerer (a, b) for elementet a i L,
# hvis der for b i L gælder, at a < b. Vi sorterer også elementerne for at
# tage højde for, at vi f.eks. har 'L1' < 'L10' < 'L11' < ... < 'L2'.
def pairs(L):
    return sorted([(a, b) for a in L for b in L if a < b])


# Printer parene der er i generate_labels(n).
print(("Her er alle parene hvor a < b, for alle % s labels: \n" % x),
      pairs(generate_labels(x)), "\n")

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
print("Her er alle canonical triplets for listerne A1 og B1, som er",
      ("genereret fra de % s labels: \n" % x), canonical_triplets(A1, B1),
      "\n")


"""
Opgave e) - anchored_triplets(L, R)
"""


# Vi definerer anchored_triplets(L, R) som finder alle canonical triplets,
# der er anchored til en node, hvor det venstre subtree indeholder alle labels
# i listen L og tilsvarende for det højre subtree. Vi anvender funktionen
# canonical_triplets(A, B) fra opgave d), og tilføjer alle canonical triplets
# der bliver lavet, hvis man bytter om på A og B.


def anchored_triplets(L, R):
    return [y for x in [canonical_triplets(L, R), canonical_triplets(R, L)] for
            y in x]


# Vi printer alle anchored triplets for A1 og B1.
print("Her er alle anchored triplets for listerne A1 og B1, som er genereret",
      ("fra de % s labels: \n" % x), anchored_triplets(A1, B1), "\n")
