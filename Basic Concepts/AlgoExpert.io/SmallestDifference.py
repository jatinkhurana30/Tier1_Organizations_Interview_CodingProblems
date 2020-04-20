"""Smallest Difference pair of values between two unsorted Arrays Given two arrays of integers, compute the pair of
values (one value in each array) with the smallest (non-negative) difference. Return the difference.

Examples :

Input :
1 3 15 11 2
23 127 235 19 8

Output : 3
That is, the pair (11, 8)

Input : A[] = {l0, 5, 40}
        B[] = {50, 90, 80}
Output : 10
That is, the pair (40, 50)
"""

A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

A.sort()
B.sort()

a = b = 0

valid_pair = [0, 0, 1000]
while True:
    if abs(A[a] - B[b]) < valid_pair[2]:
        valid_pair[0] = A[a]
        valid_pair[1] = B[b]
        valid_pair[2] = abs(A[a] - B[b])

    if a + 1 < len(A) and b + 1 < len(B):
        if A[a + 1] <= B[b + 1]:
            a += 1
        else:
            b += 1
    else:
        break

answer = (valid_pair[0], valid_pair[1])
print(answer)