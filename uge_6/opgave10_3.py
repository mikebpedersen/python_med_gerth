"""

Exercise 10.3 (string sorting)
Write a function str_sort that sorts a list of strings, such that the strings
are sorted with respect to the number of distinct letters ('a' - 'z') there
are in the strings. Strings with an equal number of distinct letters after
converting to lower case should apper in alphabetical order.

Example:
str_sort(['AHA', 'Oasis', 'ABBA', 'Beatles',
'AC/DC', 'B. B. King','Bangles', 'Alan Parsons'])

should return ['ABBA', 'AHA', 'AC/DC', 'Oasis',
'B. B. King', 'Beatles', 'Alan Parsons', 'Bangles'].


Hint. Use len(set(X)) to find the number of different elements in a list X.

"""

import re


def str_sort(L):
    return sorted(L, key=lambda s:
                  (len(set(re.sub('[^a-z] + ', '', s.lower()))), s))
