"""
Largest Sum Contiguous Subarray
Write an efficient program to find the sum of contiguous subarray within a one-dimensional array of numbers which has the largest sum.

https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/

Input: -2, -3, 4, -1, -2, 1, 5, -3
Output: 7

"""

input_array = list(map(int, input().split(', ')))

max_here = 0
max_so_far = 0
end_index = -1
start_index = 0

for i in range(0, len(input_array)):
    max_here += input_array[i]
    if max_here < 0:
        max_here = 0
        start_index = i + 1

    if max_so_far < max_here:
        max_so_far = max_here
        end_index = i

print(max_so_far, input_array[start_index:end_index+1])
