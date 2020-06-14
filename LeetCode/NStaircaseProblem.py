"""
From: https://www.dailycodingproblem.com/

There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a function that returns
the number of unique ways you can climb the staircase. The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:

1, 1, 1, 1

2, 1, 1

1, 2, 1

1, 1, 2

2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a set of positive
integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. Generalize your function to
take in X. """


def uniqueWaysOfClimbing(n, cache, steps):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n in cache:
        return cache[n]
    elif n < 0:
        return 0

    uniqueWays = 0
    for step in steps:
        uniqueWays += uniqueWaysOfClimbing(n - step, cache, steps)

    cache[n] = uniqueWays
    return cache[n]


print(uniqueWaysOfClimbing(5, {}, [1, 2, 5]))
