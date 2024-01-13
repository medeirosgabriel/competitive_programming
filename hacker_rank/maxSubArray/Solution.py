#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def maxSubarray(arr):
    n, sub_seq = len(arr), 0
    dp = [0] * n
    dp[0] = arr[0]
    sub_arr, sub_seq = dp[0], arr[0]
    for i in range(1, n):
        sub_seq = max(sub_seq + arr[i], sub_seq, arr[i])
        dp[i] = max(dp[i - 1] + arr[i], arr[i])
        sub_arr = max(sub_arr, dp[i])
    return [sub_arr, sub_seq]