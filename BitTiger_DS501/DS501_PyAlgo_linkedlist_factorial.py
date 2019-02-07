def factorial(n):
    if n == 0:
        return 1
    if n == 1:
        return 1

    result = n * factorial(n-1)
    return result

def combination(n, k):
    return factorial(n) / (factorial(n-k) * factorial(k))
