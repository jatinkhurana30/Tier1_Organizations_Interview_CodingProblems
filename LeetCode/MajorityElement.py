"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3
Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2
"""


class Solution:
    def majorityElement(self, nums):
        majority_element = nums[0]
        majority_count = 1
        for i in range(1, len(nums)):
            if nums[i] == majority_element:
                majority_count += 1
            else:
                majority_count -= 1

            if majority_count == 0:
                majority_element = nums[i]
                majority_count = 1
        return majority_element