#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Exercise 8.5* (subtree extraction)
Make a recursive function extract(tree, leaves) that takes a binary tree tree
and a set of leaves, generates a new binary tree only containing the leaves in
leaves, i.e. repeatedly all other leaves are pruned, previous internal nodes
with no children are removed, and previous internal nodes with only one child
are replaced by the child.

Example. extract(((('a','b'),'c'),((('d','e'),'f'),'g')),{'a','c','d','f','g'})
should return (('a','c'),(('d','f'),'g'))

(see illustration below where leaves 'b' and 'e' have been removed).

           before                   after
             /\                       /\          
            /  \                     /  \
           /    \                   /    \
          /      \                 /\     \
         /        \               /  \     \
        /          \            'a'  'c'   /\
       /            \        	          /  \
      /\            /\       	         /    \
     /  \          /  \      	        /\    'g'
    /    \        /    \               /  \
   /\    'c'     /\     \            'd'  'f'
  /  \          /  \    'g'
'a'  'b'       /    \
              /\    'f'
             /  \
           'd'  'e'
"""

