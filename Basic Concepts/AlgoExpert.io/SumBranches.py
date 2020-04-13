"""
Sum of all the numbers that are formed from root to leaf paths
Given a binary tree, where every node value is a Digit from 1-9 .Find the sum of all the numbers which are formed from root to leaf paths.
For example consider the following Binary Tree.

           6
       /      \
     3          5
   /   \          \
  2     5          4
      /   \
     7     4
  There are 4 leaves, hence 4 root to leaf paths:
   Path                    Number
  6->3->2                   632
  6->3->5->7               6357
  6->3->5->4               6354
  6->5>4                    654
Answer = 632 + 6357 + 6354 + 654 = 13997
"""


class BST:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


# Driver Code to construct BST
root_node = BST(6)
root_node.left_node = BST(3)
root_node.right_node = BST(5)
root_node.left_node.left_node = BST(2)
root_node.left_node.right_node = BST(5)
root_node.right_node.right_node = BST(4)
root_node.left_node.right_node.left_node = BST(7)
root_node.left_node.right_node.right_node = BST(4)
root_node.right_node.right_node = BST(4)


def calculate_sum_of_branches(root, branch_list):
    if root is None:
        return branch_list
    if root.left_node is None and root.right_node is None:
        print(sum(branch_list) + root.data)
        return branch_list
    else:
        branch_list.append(root.data)
        branch_list = calculate_sum_of_branches(root.left_node, branch_list)
        calculate_sum_of_branches(root.right_node, branch_list)
        branch_list.remove(root.data)
        return branch_list


calculate_sum_of_branches(root_node, []) 
