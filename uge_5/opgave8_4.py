#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 8.4* (validate leaf-labeled binary trees)

Assume we want to represent binary trees, where each leaf has a string as a
label, by a nested tuple. We require the leaves are labeled with distinct
non-empty strings and all non-leaf nodes have exactly two children.

E.g. is the following such a valid binary tree.

((('A', 'B'), 'C'), ('D', ('F', 'E')))


Write a function validate_string_tuple(t) that checks, i.e. returns
True or False, if the value t is a tuple only containing distinct strings,
e.g. ('a', 'b', 'c').

"""


def validate_string_tuple(t):
    if isinstance(t, tuple):
        return [True for i in range(len(t))] == [isinstance(a, str) for a in set(t)]
    else:
        return False


t = ('A', 'B')
print(validate_string_tuple(t))

"""

Write a recursive function valid_binary_tree(t) program that checks,
i.e. returns True or False, if a value is a recursive tuple representing a
binary tree as described above.

Hint. Use the method isinstance to check if a value is of class tuple or a str,
and solve (b) using a recursive function. Collect all leaf labels in a list,
and check if all leaves are distinct by converting to set.

"""

def valid_binary_tree(t):
    b = []
    print(validate_string_tuple(t))
    if validate_string_tuple(t):
        if len(t) == 2:
            for i in t:
                if isinstance(i, tuple):
                    valid_binary_tree(i)
        b.append(t)
        print(b)
        print(validate_string_tuple(tuple(b)))
    return b

t = ((('A', 'B'), 'C', 'G'), ('D', ('F', 'E')))
print(valid_binary_tree(t))
