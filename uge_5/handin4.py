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

x = int(input("Skriv her, hvor mange strenge du vil have: "))

while x <= 0:
    x = int(input("Du skal have over 0 strenge, prøv igen: "))



def generate_labels(n):
    return [("L%s" % (i+1)) for i in range(n)]


def permute(L):
    return [L.pop(randint(0, i)) for i in range(0, len(L))[::-1]]


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
    if len(L) == 1:
        return L[0]

    r_len = randint(1, len(L)-1)

    return tuple(generate_tree(elm) for elm in (L[:r_len], L[r_len:]))


print(generate_tree(generate_labels(x)))

"""
Make a recursive function generate_triplets(T) that returns a pair
(labels, triplets) where labels is a list of all leaf labels of T, and
triplets is a list of all canonical triplets anchored at some node of T.

Hint. Use isinstance(T, str) to check if T is a leaf.

Example: For the tree (a) in part I of this exercise
generate_triplets(((('A','F'),'B'),('D',('C','E')))) should return the
following pair consisting of a list with the 6 leaf labels, and a list with
the 20 canonical triplets anchored in the tree.
(['A', 'F', 'B', 'D', 'C', 'E'],
[('B', ('A', 'F')), ('D', ('C', 'E')), ('A', ('D', 'E')), ('A', ('C', 'D')),
('A', ('C', 'E')), ('F', ('D', 'E')), ('F', ('C', 'D')), ('F', ('C', 'E')),
('B', ('D', 'E')), ('B', ('C', 'D')), ('B', ('C', 'E')), ('D', ('A', 'F')),
('D', ('A', 'B')), ('D', ('B', 'F')), ('C', ('A', 'F')), ('C', ('A', 'B')),
('C', ('B', 'F')), ('E', ('A', 'F')), ('E', ('A', 'B')), ('E', ('B', 'F'))])
"""
"""
    for subtree in T:
        if isinstance(subtree, tuple):
            return find_subtree(subtree)
        elif isinstance(subtree, str):
        
    if isinstance(T, tuple):
        return [anchored_triplets(i, j) for i, j in T]
    else:
        return [find_subtree(i) for i in T]
"""
"""
def generate_triplets(T):

    def find_subtree(T):
        if isinstance(T, tuple):
            return [find_subtree(i) for i in T]
        else:
            return [i for i in T]
    
    
    def find_labels(T, labels=None):

        if labels is None:
            labels = []

        if isinstance(T, str):
            print(T)
            labels.append(T)
            print(labels)

        else:
            for elm in T:
                print(elm)
                find_labels(elm, labels)
                
        return labels
    
    
    return (find_labels(T))


print(generate_triplets(((('A', 'F'), 'B'), ('D', ('C', 'E')))))
"""
"""
Make a function triplet_distance(T1, T2) that computes the triplet distance
between the trees T1 and T2.

Hint. Recall that the triplet distance equals n(n-1)(n-2)/6 minus the number
of common triplets between T1 and T2, and use Python set to handle the sets
of computed triplets.

Example: For the two trees above
triplet_distance(((('A','F'),'B'),('D',('C','E'))),
(((('D','A'),'B'),'F'),('C','E')) should return 10.
"""

def triplet_distance(T1, T2):

    n = len(generate_triplets(T1[0]))
    equation = n * (n-1) * (n-2) // 6
    
    common = [x for x in generate_triplets(T1)[1] for y in generate_triplets(T2)[1] if x == y]

    return equation - len(common)

"""
What is the order of the tree sizes you can handle with generate_tree and
triplet_distance in reasonable time - say about 10 seconds? Tens, hundreds,
thousands, millions... of leaves? Use the function generate_tree to generate
random trees of increasing sizes and measure the time for generate_tree and
triplet_distance separately.
"""

from time import time
import matplotlib.pyplot as plt

labels, compute_time = [], []

def check_time(y):
    for i in range(1, y+1):
        blabla = generate_labels(i)
        x = len(blabla)
        start = time()
        generate_tree(blabla)  # the computation we time
        end = time()
        t = end - start
        print("i =", i, "x =", y, "time(sec) =", t)
        labels.append(x)
        compute_time.append(t)

    plt.title('Generating Random Trees')
    plt.xlabel('Amount of labels')
    plt.ylabel('computation time (seconds)')
    plt.plot(labels, compute_time, "g:")
    plt.plot(labels, compute_time, "ro")
    plt.show()

#print(check_time(x))

"""
(Optional) Make a function print_ascii_tree(T) to print trees like the ones
shown in part I of this exercise.
"""
