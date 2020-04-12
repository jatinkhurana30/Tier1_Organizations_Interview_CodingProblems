"""
Here we use the memoization to build a cache in our recursion for our fibonacci code
"""

fibonacci_index = int(input())


def calculate_fib(n, cache):
    if n in cache.keys():
        return cache[n]
    cache[n] = calculate_fib(n - 1, cache) + calculate_fib(n - 2, cache)
    return cache[n]


fib_cache = {1: 1, 2: 1}
print(calculate_fib(fibonacci_index, fib_cache))
