"""
4Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:

    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:

    1
   / \
  2   2
   \   \
   3    3
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        if root is None:
            return True
        elif root.left is None and root.right is None:
            return True
        elif root.left is None or root.right is None:
            return False
        else:
            return self.compareNodes(root.left, root.right)

    def compareNodes(self, left, right):
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        elif left.val == right.val:
            return self.compareNodes(left.left, right.right) and self.compareNodes(left.right, right.left)




