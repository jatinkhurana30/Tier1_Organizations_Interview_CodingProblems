"""
Reverse bits of a given 32 bits unsigned integer.



Example 1:

Input: 00000010100101000001111010011100
Output: 00111001011110000010100101000000
Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
Example 2:

Input: 11111111111111111111111111111101
Output: 10111111111111111111111111111111
Explanation: The input binary string 11111111111111111111111111111101 represents the unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
"""

n = 8
str = "A man, a plan, a canal: Panama"

i = 0
while i < len(str):
    if str[i].isspace() or (not str[i].isalnum()):
        str = str[0:i] + str[i + 1:]
        i -= 1
    i += 1


def isPalindrome(string):
    i = 0
    while i < len(string) // 2:
        if string[i].lower() != string[len(string)-1-i].lower():
            return False
        i += 1

    return True
print(str)

print(isPalindrome(str))


class Solution:
    def isPalindrome(self, s: str) -> bool:
        if str == "":
            return False

        i = 0
        while i < len(str):
            if str[i].isspace() or (not str[i].isalnum()):
                str = str[0:i] + str[i + 1:]
                i -= 1
            i += 1

        return self.isPalindrome(str)

    def isPalindrome(self, string):
        i = 0
        while i < len(string) // 2:
            if string[i].lower() != string[len(string) - 1 - i].lower():
                return False
            i += 1

        return True
