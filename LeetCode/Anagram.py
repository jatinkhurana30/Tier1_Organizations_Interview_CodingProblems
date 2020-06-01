"""

Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
Note:
You may assume the string contains only lowercase alphabets.

Follow up:
What if the inputs contain unicode characters? How would you adapt your solution to such case?
"""
from collections import defaultdict


def isAnagram( s: str, t: str) -> bool:

    hash_map = defaultdict(lambda: 0)
    for i in range(0, len(s)):
        if hash_map.__contains__(s[i]):
            hash_map[s[i]] += 1
        else:
            hash_map[s[i]] = 1

    j = 0
    while j < len(t):
        if hash_map[t[j]] > 1:
            hash_map[t[j]] -= 1
        elif hash_map[t[j]] == 1:
            hash_map.pop(t[j])
        else:
            return False
        j += 1

    return True


print(isAnagram("cata", "ctaa"))



