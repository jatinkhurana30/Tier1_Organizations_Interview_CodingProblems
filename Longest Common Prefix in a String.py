"""
Given a array of N strings, find the longest common prefix among all strings present in the array.

Input:
The first line of the input contains an integer T which denotes the number of test cases to follow. Each test case contains an integer N. Next line has space separated N strings.

Output:
Print the longest common prefix as a string in the given array. If no such prefix exists print "-1"(without quotes).


Sample Input:
geeksforgeeks geeks geek geezer

Output : gee
"""

array_of_strings = input().split(' ')
min_length = 999
smallest_string = None

# We find the smallest string in the array of string and it's length
for string in array_of_strings:
    if len(string) < min_length:
        smallest_string = string
        min_length = len(string)


# Now we simply start comparing the starting index of each string in that array to the indexes of smallest string
longest_common_substring = ''
for i in range(0, min_length):
    flag = 0
    for string in array_of_strings:
        if string[i] != smallest_string[i]:
            flag = 1

    # If we were not able to find any dissimilarity of a character in all the strings of array,
    # we simply add it to out output 
    if flag != 1:
        longest_common_substring += smallest_string[i]

if longest_common_substring == '':
    print('-1')
else:
    print(longest_common_substring)
