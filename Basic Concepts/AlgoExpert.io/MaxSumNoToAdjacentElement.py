"""
Maximum sum such that no two elements are adjacent | Set 2
Given an array of positive numbers, find the maximum sum of a subsequence with the constraint that no 2 numbers in the sequence should be adjacent in the array. So 3 2 7 10 should return 13 (sum of 3 and 10) or 3 2 5 10 7 should return 15 (sum of 3, 5 and 7).

Examples:

Input :  arr[] = {3, 5, 3}
Output : 6
Explanation :
Selecting indexes 0 and 2 will maximise the sum
i.e 3+3 = 6

Input : arr[] = {2, 5, 2}
Output : 5
"""

array = list(map(int, input().split(', ')))


def getMaxSumNoAdjacentValues(input_array):
    i = 0
    max_sum = 0
    while i < len(input_array):
        j = i + 2
        while j < len(input_array):
            if max_sum < input_array[i] + input_array[j]:
                max_sum = input_array[i] + input_array[j]
            j += 1
        i += 1
    return max_sum


print(getMaxSumNoAdjacentValues(array))
