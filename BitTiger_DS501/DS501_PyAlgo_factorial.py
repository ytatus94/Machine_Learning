def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    return n * factorial(n-1)

def combination(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))

memo = {}

def factorial_memo(n):
    if n in memo:
        return memo[n]
    if n == 0:
        memo[0] = 1
        return 1

    result = n * factorial(n-1)
    memo[n] = result
    return result

def combination_memo(n, k):
    return factorial_memo(n) / (factorial_memo(n-k) * factorial_memo(k))

import timeit
import sys
sys.setrecursionlimit(2000)

print('Run combination(1000, 500) 1 time:')
print(timeit.timeit('combination(1000, 500)', globals=globals(), number=1))
print(timeit.timeit('combination_memo(1000, 500)', globals=globals(), number=1))
