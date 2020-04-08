"""
Infinite Monkey Theorem

Problem Statement: We need to find the minimum number of spaces we can insert in the input string such that the
resulting numbers are part of the list of numbers provided in the 2nd line of input

Sample Input:
3141592653589793238462643383279
314 49 9001 15926535897 14 9323 8462643383279 4 793 3141 5926535897 93238462643383279

Sample Output: 2

Explanation:
3141 5926535897 93238462643383279
By inserting 2 spaces , we are able to get the numbers present in the list of numbers.
Other options are also available by we need to minimize the space count
"""

input_string = input()
input_string_lists = input().split(' ')

substrings_of_input_string = []

for string in input_string_lists:
    if input_string.__contains__(string):
        substrings_of_input_string.append(string)


# Function to check if substring is present in the starting of a input string
def substring_starts_from_index_0(main_string, substring):
    if main_string[0:len(substring)] == substring:
        return True
    else:
        return False


# The recursion function which will build a Tree data structure and store all possible combinations of substrings
# which complete the input strings
def calculate_spaces(input_str, sub_strings, tree_patterns):
    if len(input_str) == 0 or input_str is None:
        return tree_patterns

    candidate_substrings = []
    for sub_str in sub_strings:
        if substring_starts_from_index_0(input_str, sub_str):
            candidate_substrings.append(sub_str)

    for candidate in candidate_substrings:
        available_substrings = sub_strings[:]
        available_substrings.remove(candidate)
        new_node = Tree(candidate)
        tree_patterns.add_child(new_node)
        calculate_spaces(input_str[len(candidate):], available_substrings, new_node)

    return tree_pattern


# An implementation of tree data structure, which can have any number of children
class Tree:
    def __init__(self, data):
        self.children = []
        self.data = data

    def add_child(self, child):
        self.children.append(child)

    def get_child(self):
        return self.children

    # The method which will return the shortest path to a lead, or minimum depth of a tree, this will help find the
    # minimum words required to complete the input string
    @staticmethod
    def get_minimum_level(root):
        if root.children is None or len(root.children) == 0:
            return 1
        else:
            minimum_distance = []
            for child in root.children:
                minimum_distance.append(Tree.get_minimum_level(child) + 1)

            return min(minimum_distance)


# Driver code
tree_pattern = Tree('Root')

# We subtract 2 from depth of tree as 1 node is the root node common for all branches, and another as number of
# spaces = number of words -1
calculate_spaces(input_string, substrings_of_input_string, tree_pattern)
print(Tree.get_minimum_level(tree_pattern) - 2)
