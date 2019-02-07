import timeit

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))
print(fibonacci(6))
print(fibonacci(7))
print(fibonacci(8))

memo = {}

def fibonacci_memo(n):
    if n in memo:
        return memo[n]
    elif n == 0:
        memo[0] = 0
        return 0
    elif n == 1:
        memo[1] = 1
        return 1

    result = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    memo[n] = result
    return result

print(timeit.timeit('fibonacci(30)', globals=globals(), number=1))
print(timeit.timeit('fibonacci_memo(30)', globals=globals(), number=1))

def fibonacci_tabulation(n):
    table = [0] * (n+1)
    table[0] = 0
    table[1] = 1
    for i in range(2, n+1):
        table[i] = table[i-1] + table[i-2]
    return table[n]

print(fibonacci_tabulation(10))

def fibonacci_tabulation_optimized(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a
