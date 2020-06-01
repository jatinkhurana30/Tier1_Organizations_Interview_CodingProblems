"""
Given an array containing n distinct numbers taken from 0, 1, 2, ..., n, find the one that is missing from the array.

Example 1:

Input: [3,0,1]
Output: 2
Example 2:

Input: [9,6,4,2,3,5,7,0,1]
Output: 8
Note:
Your algorithm should run in linear runtime complexity. Could you implement it using only constant extra space complexity?
"""
def missingNumber(nums):
    max = 0
    found_zero = 0
    actual_sum = 0
    for item in nums:
        if max < item:
            max = item
        if item == 0:
            found_zero = 1
        actual_sum += item

    if max != len(nums) - 1:
        return len(nums) - 1

    if max != len(nums):
        return len(nums)

    if found_zero == 0:
        return 0

    expected_sum = 0
    for i in range(0, max + 1):
        expected_sum += i

    if expected_sum - actual_sum != 0:
        return expected_sum - actual_sum

    return -1


print(missingNumber([1, 2]))