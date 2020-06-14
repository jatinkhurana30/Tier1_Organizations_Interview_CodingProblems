"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: ["flower","flow","flight"]
Output: "fl"
Example 2:

Input: ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


class Solution:
    def longestCommonPrefix(self, strs):
        return self.divideArrayForLCP(strs)

    def divideArrayForLCP(self, array):

        if len(array) <= 1:
            return array

        mid = len(array) // 2
        left = self.divideArrayForLCP(array[0:mid])
        right = self.divideArrayForLCP(array[mid:])
        return self.getLCP(left[0], right[0])

    def getLCP(self, str1, str2):
        n = 0
        if len(str1) <= len(str2):
            n = len(str1)
        else:
            n = len(str2)
        i = 0
        lcp = ""
        while i < n:
            if str1[i] == str2[i]:
                lcp += str1[i]
            else:
                break
            i += 1
        return [lcp]


print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
