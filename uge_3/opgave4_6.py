#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb  5 14:23:02 2020

@author: JensTrolle
"""

print("This program gives you a multiplication",
      "table of a dimension between 1 and 100.")

# Check for correct dimension size
x = int(float(input("Write the dimension of the multiplication table: ")))
while x > 100 or x < 1:
    x = int(float(input("The dimension has to be between 1 and 100: ")))

longest_num = len(str(x ** 2))

# Define upper_line
upper_line = ["  *", "|"]

# Adds numbers from 0 to x to upper_line.
for i in range(0, x+1):
    i = ('{:%sd}' % longest_num).format(i)
    upper_line.append(i)

# Joins upperline with spaces and prints it.
upper_line_join = " ".join(map(str, upper_line))
print(upper_line_join)

# Defines line and adds horizontal lines until it has reached the length
# of upper_line_join.
line = []
for i in range(0, len(upper_line_join)):
    line.append('-')
join_line = ''.join(line)
print(join_line)

"""
For every number between 0 and x, we first store the value of i in k, and
format i, so that it has space for len(100) = 3. Then we add i to the list
numbers, and append a vertical line. We then set multiples_lines and
final_join, so we can iterate them with numbers in the next for loop.
We start by multiplying the stored value of i with j, and then formatting
it, so we have space for len(100*100) = 5. We then append this number to
multiples_line until we are not in the range anymore.
then we join everything in multiples_line with spaces, and print it. Then the
first for loop continues, if we are still in the range.
"""
for i in range(0, x+1):
    k = i
    i = '{:3d}'.format(i)
    numbers = [i]
    numbers.append(' | ')
    join_numbers = "".join(map(str, numbers))
    print(join_numbers, end="")

    multiples_line = []
    for j in range(0, x+1):
        multiples = k * j
        multiples = ('{:%sd}' % longest_num).format(multiples)
        multiples_line.append(multiples)
    final_join = " ".join(map(str, multiples_line))
    print(final_join)
