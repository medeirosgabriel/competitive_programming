'''
Top-down (memoization): starting from the optimal general solution that
you want to find and then analyze which subproblems are necessary to 
resolve until a subproblem with trivial resolution.
'''

def fibonacci(n, table):
    if (n == 0): return 0
    elif (n == 1): return 1
    else: 
      return fibonacci(n - 1, table) + fibonacci(n - 2, table)

n = 11
print(fibonacci(n, {}))
