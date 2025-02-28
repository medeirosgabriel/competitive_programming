#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'powerSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER X
#  2. INTEGER N
#

def backtracking(x, n, start):
    if (x < 0): return 0
    if (x == 0): return 1
    count = 0
    i = start + 1
    while (math.pow(i, n) <= x):
        count += backtracking(x - math.pow(i, n), n, i)
        i += 1
    return count
        

def powerSum(X, N):
    # Write your code here
    return backtracking(X, N, 0)
