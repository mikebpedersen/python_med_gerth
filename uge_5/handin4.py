'''
HANDIN 4: Triplet Distance (Part II)


Afleveringen er lavet af:
    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflektion:
'''
# Her er alle funktionerne fra handin3:

from random import randint

def generate_labels(n):
    return [("L%s" % (i+1)) for i in range(n)]

def pairs(L):
    return sorted([(a, b) for a in L for b in L if a < b])


def canonical_triplets(A, B):
    return[(i, j) for i in A for j in pairs(B)]


def anchored_triplets(L, R):
    return canonical_triplets(L, R) + canonical_triplets(R, L)


"""
Opgave a) - Lav generate_tree(L), som genererer tilfældige træer fra en liste.
"""

# Vi definerer funktionen, som returnerer det 1. element af listen, hvis listen
# har længde 1. Så finder vi et tilfældigt tal mellem 1 og længden af L - 1,
# som vi kan bruge til at vælge længden af hver side af træet.
# Så returnerer vi en tuple hvor vi anvender funktionen igen på L, som vi har
# delt op i to lister af tilfældig længde. Idet vi kun terminerer når L har
# længde 1, så sikrer vi os, at vi kun genererer binære træer.


def generate_tree(L):
    if len(L) == 0:
        return None

    if len(L) == 1:
        return L[0]

    else:
        r_len = randint(1, len(L)-1)
        return tuple(generate_tree(elm) for elm in (L[:r_len], L[r_len:]))


"""
Opgave b) - Lav generate_triplets(T), som returnerer labels og triplets for et
            træ.
"""

# Vi definerer generate_triplets(T), som først tjekker om vores træ er en str,
# hvis ja, så er vi i slutningen af vores træ, og kan returnere strengen og en
# tom liste, som vi kan bruge rekursivt. 
# Vi deler så træet i to, og anvender retursivt vorse funktion, så vi kan komme
# ned i bunden af træet, og lægger derefter de nye labels til en tom liste, 
# labels. Så returnerer vi labels for træet, samt alle anchored triplets for
# hver side af træet.


def generate_triplets(T):
    if isinstance(T, str):
        return [T], []
    labels = []
    triplets_left = generate_triplets(T[0])
    triplets_right = generate_triplets(T[1])
    labels += triplets_left[0] + triplets_right[0]
    return (labels,
            (anchored_triplets(triplets_left[0], triplets_right[0])
             + triplets_left[1] + triplets_right[1]))


"""
Opgave c) - Lav triplet_distance(T1, T2), som beregner triplet-distance mellem
            to træer.
"""

# Inputtet til triplet_distance er de to træer, som vi vil måle forskellen på.
# n er hvor mange labels vi har, og equation er den ligning, som vi fik givet
# i opgavebeskrivelsen. I variablen common finder vi alle de triplets som
# opstår i begge træer. Returnerer vi forskellen længden af common fra
# equation, så vi finder triplet distance mellem de to træer.

def triplet_distance(T1, T2):

    n = len(generate_triplets(T1)[0])
    equation = n * (n-1) * (n-2) // 6

    common = [x for x in generate_triplets(T1)[1] 
                for y in generate_triplets(T2)[1] if x == y]

    return equation - len(common)


"""
What is the order of the tree sizes you can handle with generate_tree and
triplet_distance in reasonable time - say about 10 seconds? Tens, hundreds,
thousands, millions... of leaves? Use the function generate_tree to generate
random trees of increasing sizes and measure the time for generate_tree and
triplet_distance separately.
"""

# Vi importerer time fra time, så vi kan måle hvor lang tid det tager at
# generere træer af voksende størrelse og at finde triplet distance af disse.
# Vi definerer check_time_*(y), som måler hvor lang tid det tager at anvende
# funktionen, ved at tage forskellen mellem tiden før vi kører funktionen, og
# tiden efter vi kører funktionen. Vi kører dette i en range fra 0 til y.
# Dette kan også gøres med spring af en størrelse, (n < y), så vi hurtigere
# kan komme hen til træer af større størrelse. For hvert i i rangen tjekker vi
# om vi har nået et nyt maks, hvis vi har det, så printer vi størrelsen af
# træet, og hvor lang tid det tog. Hvis vi når vores threshold, så stopper
# vi med at tjekke.


from time import time


def check_time_tree(y, compute=0):

    n = int(input("Write the step-size you want here: "))
    while n < 1:
        n = int(input("Input a step-size above 0: "))

    th = 10

    for i in range(0, y+1, n):
        if i == 0:
            next
        else:
            start = time()
            generate_tree(generate_labels(i))
            end = time()
            t = end - start

            if t > th:
                return print("We have reached our threshold of %s s.," % (th),
                             "with a length of %s," % (i),
                             "and a time(sec) of %s." % (t))

            if t >= compute:
                compute = t
                print("Length of tree with the longest compute time(sec)"
                      " so far is: %s," % (i), " with time: %.5f." % t)

    return print("We did not hit our threshold of %s" % (th),
                 "seconds with %s labels." % (y))


x = int(input("How many labels do you want to check compute time for? "))

while x < 1:
    x = int(input("Input #labels above 0: "))


check_time_tree(x)

def check_time_triplets(y, compute=0):

    n = int(input("Write the step-size you want here: "))
    while n < 1:
        n = int(input("Input a step-size above 0: "))

    th = 10

    for i in range(0, y+1, n):
        if i == 0:
            next
        else:
            start = time()
            triplet_distance(generate_tree(generate_labels(i)),
                             generate_tree(generate_labels(i)))
            end = time()
            t = end - start

            if t > th:
                return print("We have reached our threshold of %s s.," % (th),
                             "with a length of %s," % (i),
                             "and a time(sec) of %s." % (t))

            if t >= compute:
                compute = t
                print("Length of tree with the longest compute time(sec)"
                      " for triplets so far is: %s," % (i), 
                      " with time: %.5f." % t)

    return print("We did not hit our threshold of %s" % (th),
                 "seconds with %s labels." % (y))


x = int(input("How many labels do you want to check compute time for triplet",
              "distance for? "))

while x < 1:
    x = int(input("Input #labels above 0: "))


check_time_triplets(x)

# Vi har observeret, at vi kan klare at generere træer på ca. 2*10^6 labels
# på 10 sekunder. Hvis vi også skal lave triplet distance, så kan vi kun
# håndtere ca. 3*10^1 labels.

"""
(Optional) Make a function print_ascii_tree(T) to print trees like the ones
shown in part I of this exercise.
"""
