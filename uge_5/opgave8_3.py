#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 8.3 (tree relabeling)

Make a recursive function relabel(tree, new_names) that takes a tree tree and
a dictionary new_names = { old_name : new_name, ... }, and returns a new tree
where labels in the dictionary new_names are replaced by the corresponding
values in the dictionary. Leaves not in the dictionary remain unchanged.

Example: relabel(('a', ('b', 'c')), {'a': 'x', 'c': 'y'}) should return
('x', ('b', 'y')).

"""
