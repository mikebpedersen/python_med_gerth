#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 09:32:13 2020

@author: JensTrolle
"""

import matplotlib.pyplot as plt
from math import sqrt


def koch(p, q, depth=3):
    if depth == 0:
        return [p, q]
    else:
        dx, dy = q[0] - p[0], q[1] - p[1]
        h = 1 / sqrt(12)
        p1 = p[0] + dx / 3, p[1] + dy / 3
        p2 = p[0] + dx / 2 - h * dy, p[1] + dy / 2 + h * dx
        p3 = p[0] + dx * 2 / 3, p[1] + dy * 2/ 3
        return (koch(p, p1, depth - 1)[:-1]
                + koch(p1, p2, depth - 1)[:-1]
                + koch(p2, p3, depth - 1)[:-1]
                + koch(p3, q, depth - 1))


points = koch((0, 1), (0, 0), depth=4)
X, Y = zip(*points)

plt.subplot(aspect='equal')
plt.plot(X, Y, 'r-')
plt.plot(X, Y, 'k.')
plt.show()
