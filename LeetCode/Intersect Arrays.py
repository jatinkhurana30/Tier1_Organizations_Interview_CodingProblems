"""
Given two arrays, write a function to compute their intersection.

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]
Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Note:

Each element in the result should appear as many times as it shows in both arrays.
The result can be in any order.
"""
from collections import Counter


def intersect(nums1, nums2):
    nums1_dict = Counter(nums1)
    answer = []
    for item in nums2:
        if nums1_dict.get(item) and nums1_dict.get(item) > 0:
            answer.append(item)
            nums1_dict[item] -= 1

    return answer


print(intersect([4, 9, 5], [9, 4, 9, 8, 4]))
