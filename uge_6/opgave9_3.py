#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Exercise 9.3 (maze path)
In this exercise you should code a recursive maze solver, that does a recursive
search for the path from "A" to "B" in a rectangular maze. The program should
read from input a maze represented by first a single line containing two
numbers, the number of rows n and columns m of the maze, followed by n rows
each containing a string of length m representing the maze, where "#" is a
blocked cell, "A" denotes the start cell, "B" the end cell, and "." a free cell
("A" and "B" are also free cells). Given a free cell one can move to an
adjacent free cell horizontally and vertically but not diagonally.

An example input:

11 19
#######A###########
#.......#.#...#...#
#.###.###...#.#.#.#
#...#.....#.#...#.#
#.#.###.#.#.#.###.#
#.#.....#...#.#...#
#.###########.#.#.#
#.#.#.....#...#.#.#
#.#.#####.#####.#.#
#.........#.....#.#
###############B###

The program should output the string "no path" if there exist no path from A
to B in the maze. If there exists a path, a solution should be printed with "x"
marking the path from A to B. A possible solution to the above maze is:

#######A###########
#....xxx#.#xxx#xxx#
#.###x###xxx#x#x#x#
#...#xxxxx#.#xxx#x#
#.#.###.#.#.#.###x#
#.#.....#...#.#xxx#
#.###########.#x#.#
#.#.#.....#...#x#.#
#.#.#####.#####x#.#
#.........#....x#.#
###############B###

Note: In the lecture the solution only
identified if there was a path from A to B.

Hint: One solution is to modify the solution from the lecture, and only make
recursive calls when a solution has not been found yet, and to update the maze
before returning from a recursive call.

Use print('\n'.join(maze)) to print the maze.

"""
