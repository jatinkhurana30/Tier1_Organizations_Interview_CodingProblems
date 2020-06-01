"""
The count-and-say sequence is the sequence of integers with the first five terms as following:

1.     1
2.     11
3.     21
4.     1211
5.     111221
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n where 1 ≤ n ≤ 30, generate the nth term of the count-and-say sequence. You can do so recursively, in other words from the previous member read off the digits, counting the number of digits in groups of the same digit.

Note: Each term of the sequence of integers will be represented as a string.
"""


class Solution:
    def countAndSay(self, n: int) -> str:
        current = "1"
        if n == 1:
            return current

        for i in range(2, n + 1):
            new = self.readGroups(current)
            current = new

        return current

    def readGroups(self, current):
        new = []
        i = 0
        while i < len(current):
            group1 = current[i]
            count = 0
            j = i
            while j < len(current) and current[j] == current[i]:
                count += 1
                j += 1

            new.append(str(count))
            new.append(group1)
            i += count

        return ''.join(new)

print(Solution().countAndSay(4))
