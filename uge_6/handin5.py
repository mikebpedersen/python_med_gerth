#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

HANDIN 5 - Eight Queens puzzle

Afleveringen er lavet af:
    201807850 (Jens Trolle)
    201806389 (Mike Pedersen)
    201805266 (Frederik Thaibert)

Reflektion:

"""

"""

Exercise 9.4 - handin 5 (eight queens puzzle)
Write a program that solves the eight queens puzzle.
The program should solve the more general problem of solving the n queen
problem on an n x n chessboard, where n is given as input. The program should
output at least one solution if solutions exist, e.g. as below, or that there
is no solution.

Size of board: 5
Q....
..Q..
....Q
.Q...
...Q.

Hint: Write a recursive solution that generates all possible solutions,
but avoids expanding partial solutions already known to be invalid.
Since no two queens can be in the same row, a solution must have exactly one
queen in each row. A partial solution for the first i queens can be described
by a tuple of length i with the column positions for the queens in the i first
rows. E.g., the tuple (0, 2, 4) could represent a partial solution for the
first three rows of a 5 x 5 board:

column : 01234
row 0  : Q....
row 1  : ..Q..
row 2  : ....Q
row 3  : .....
row 4  : .....

One way to structure your program is to define three functions:

valid(r1, c1, r2, c2) that checks if two queens at positions (r1,c1) and
(r2,c2) respectively do not threaten each other (i.e. are in different rows
and columns and not on the same diagonal)

print_solution(solution) that prints a solution given by a list solution where
queen i is at position (i,solution(i))

solve(solution) is a recursive function that tries to expand a partial solution
given by solution for the first len(solution) queens.

"""
