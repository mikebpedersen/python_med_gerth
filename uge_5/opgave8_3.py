#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 8.3 (tree relabeling)

Make a recursive function relabel(tree, new_names) that takes a tree, tree, and
a dictionary new_names = { old_name : new_name, ... }, and returns a new tree
where labels in the dictionary new_names are replaced by the corresponding
values in the dictionary. Leaves not in the dictionary remain unchanged.

Example: relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'}) should return
('x', ('b', 'y')).

"""
"""

def relabel(tree, new_names=None):

    if new_names is None:
        return tree

    if isinstance(tree, str):
        if tree in new_names:
            print(new_names[tree])

    else:
        for child in tree:
            relabel(child, new_names)
    return tree
"""


def relabel(tree, new_names=None):
    if new_names is None:
        return tree
    if type(tree) is str:
        return new_names.get(tree, tree)
    return tuple(relabel(node, new_names) for node in tree)


print(relabel(('a', ('b', 'c'))))
