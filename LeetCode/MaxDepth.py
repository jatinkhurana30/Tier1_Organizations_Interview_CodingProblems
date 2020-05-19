"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root):
        return self.findMaxDepth(root, 0)

    def findMaxDepth(self, node, depth):
        if node == None:
            return depth
        else:
            depth += 1
            return max(self.findMaxDepth(node.left, depth), self.findMaxDepth(node.right, depth))
