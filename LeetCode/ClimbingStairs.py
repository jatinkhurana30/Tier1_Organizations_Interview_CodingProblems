"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.
"""


def climbStairs(n: int) -> int:
    return climbCounts(n, {})


def climbCounts(n, cache):
    if n in cache:
        return cache[n]
    else:
        if n == 0:
            return 1
        if n < 0:
            return 0
        else:
            cache[n] = climbCounts(n - 2, cache) + climbCounts(n - 1, cache)
            return cache[n]


print(climbStairs(35))
