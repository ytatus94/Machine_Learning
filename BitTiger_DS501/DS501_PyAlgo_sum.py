import timeit

def sum(n):
    sum = 0
    for i in range(1, n+1):
        sum += 1
    return sum

def sum2(n):
    return n*(n+1)/2

print(timeit.timeit('sum(10000)', globals=globals(), number=1000))
print(timeit.timeit('sum2(10000)', globals=globals(), number=1000))
