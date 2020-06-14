"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
             Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        answer_substring = ""
        substr = ""
        max_len = 0
        current_len = 0
        i = 0

        while i < len(s):
            if s[i] not in substr:
                substr += s[i]
                current_len += 1
            else:
                if max_len < current_len:
                    max_len = current_len
                    answer_substring = substr

                substr = s[i]
                current_len = 1
            i += 1

        if max_len < current_len:
            max_len = current_len
            answer_substring = substr
        return len(answer_substring)

print(Solution().lengthOfLongestSubstring("dvdf"))



