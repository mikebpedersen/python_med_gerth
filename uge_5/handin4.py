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


def permute(L):
    return [L.pop(randint(0, i)) for i in range(0, len(L))[::-1]]


def pairs(L):
    return sorted([(a, b) for a in L for b in L if a < b])


def canonical_triplets(A, B):
    return[(i, j) for i in A for j in pairs(B)]


def anchored_triplets(L, R):
    return canonical_triplets(L, R) + canonical_triplets(R, L)


"""
Make a recursive function generate_tree(L), that given a list of labels L,
returns a random binary tree where the list of leaf labels from left to right
in the tree equals L.

Hint: Split the list L at a random position into two nonempty parts left and
right, and recursively construct the trees for the two parts.

Example: generate_tree(['A', 'B', 'C', 'D', 'E', 'F']) could return
((('A', ('B', 'C')), ('D', 'E')), 'F')
"""

a_list = ['A', 'B', 'C', 'D', 'E', 'F']


def generate_tree(L):
    if len(L) == 1:
        return L[0]
    b = randint(1, len(L)-1)
    L_LR = L[:b], L[b:]
    return tuple(generate_tree(i) for i in L_LR)

        


print(generate_tree(a_list))

"""
Make a recursive function generate_triplets(T) that returns a pair
(labels, triplets) where labels is a list of all leaf labels of T, and
triplets is a list of all canonical triplets anchored at some node of T.

Hint. Use isinstance(T, str) to check if T is a leaf.

Example: For the tree (a) in part I of this exercise
generate_triplets(((('A','F'),'B'),('D',('C','E')))) should return the
following pair consisting of a list with the 6 leaf labels, and a list with
the 20 canonical triplets anchored in the tree.
(['A', 'F', 'B', 'D', 'C', 'E'], [('B', ('A', 'F')), ('D', ('C', 'E')),
('A', ('D', 'E')), ('A', ('C', 'D')), ('A', ('C', 'E')), ('F', ('D', 'E')),
('F', ('C', 'D')), ('F', ('C', 'E')), ('B', ('D', 'E')), ('B', ('C', 'D')),
('B', ('C', 'E')), ('D', ('A', 'F')), ('D', ('A', 'B')), ('D', ('B', 'F')),
('C', ('A', 'F')), ('C', ('A', 'B')), ('C', ('B', 'F')), ('E', ('A', 'F')),
('E', ('A', 'B')), ('E', ('B', 'F'))])
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


"""
What is the order of the tree sizes you can handle with generate_tree and
triplet_distance in reasonable time - say about 10 seconds? Tens, hundreds,
thousands, millions... of leaves? Use the function generate_tree to generate
random trees of increasing sizes and measure the time for generate_tree and
triplet_distance separately.
"""


"""
(Optional) Make a function print_ascii_tree(T) to print trees like the ones
shown in part I of this exercise.
"""
