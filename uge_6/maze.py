#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 15:46:32 2020

@author: JensTrolle
"""


def explore(i, j):
    global solution
    if (0 <= i < n and 0 <= j < m and maze[i][j] != "#" and not visited[i][j]):
        visited[i][j] = True

        if maze[i][j] == 'B':
            solution = True

        explore(i-1, j)
        explore(i+1, j)
        explore(i, j-1)
        explore(i, j+1)


def find(symbol):
    for i in range(n):
        j = maze[i].find(symbol)
        if j >= 0:
            return (i, j)


n, m = [int(x) for x in input().split()]
maze = [input() for i in range(n)]

solution = False
visited = [m*[False] for i in range(n)]

explore(*find('A'))

if solution:
    print("path from A to B exists")

else:
    print("no path")
