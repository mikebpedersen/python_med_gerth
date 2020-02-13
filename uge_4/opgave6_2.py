#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In this exercise extends Exercise 6.1.

Write a program that prints the most frequent words containing at least six
characters occuring in a text file. E.g. for the saxo.txt file it should print
something like the below:

Rank Freq. Word
====================
   1  373  should
   2  221  himself
   3  199  father
   4  196  battle
   5  187  though
   6  181  thought
   7  172  against
   8  140  before
   9  134  daughter
  10  122  country

You can use the following code to split the content of a file into a list of
lower case words, ignoring everything that is not a letter in the text.

import re
txt = open("saxo.txt").read()
txt = txt.lower()
words = re.split('[^a-z]+', txt)
Hint. Use the sorted function to sort a list of tuples of the form
(frequency, word), and try to use list comprehension to create such a list from
a frequency dictionary.
"""

