#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#

def bfs(n, m, edges, s):
    # Write your code here
    dist, visited = [-1] * n, [False] * n
    paths = [[] for _ in range(n)]
    for start, end in edges: 
        paths[start - 1].append(end - 1)
        paths[end - 1].append(start - 1)
    dist[s - 1], visited[s - 1], queue = 0, True, [s - 1]
    while (len(queue) > 0):
        node = queue.pop(0)
        for neigh in paths[node]:
            if (not visited[neigh]):
                visited[neigh] = True
                queue.append(neigh)
                if (dist[neigh] == -1 or dist[neigh] > dist[node] + 6):
                    dist[neigh] = dist[node] + 6
    dist.remove(0)
    return dist
