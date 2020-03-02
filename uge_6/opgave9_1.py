"""

Exercise 9.1 (bitonic minimum)

We call a list L=[x1, ..., xn] bitonic, if there exists a k, 1<k<n, such that
x1 > x2 > ··· > xk-1 > xk < xk+1 < ··· < xn, i.e. xk is the minimum of the
list. Write a method bitonic_min that given a list, returns the minimum of the
list. Your implementation should use binary search (i.e. you cannot use the
Python builtin min function).

Example: bitonic_min([10,7,4,2,3,5,9,11]) should return 2.

"""


def bitonic_min(L, min_so_far=None):

    min_so_far = L[0]

    for i in L:
        if i <= min_so_far:
            min_so_far = i
        else:
            return min_so_far

    return min_so_far
