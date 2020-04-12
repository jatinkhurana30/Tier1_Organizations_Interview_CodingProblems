"""Write a program that, given an array A[] of n numbers and another number x, determines whether or not there exist
two elements in S whose sum is exactly x.

Sample Input:
1 2 3 4 5
9
Output: (4,5)


1 -2 3 -4 5
-6
Output: (-2,-4)

"""

A = list(map(int, input().split(' ')))
x = int(input())


# Time Complexity = O(n)
def find_numbers(Array, X):
    my_set = set()
    for i in Array:
        if my_set.__contains__(X - i):
            print((X - i, i))
        else:
            my_set.add(i)


find_numbers(A, x)
