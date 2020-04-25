"""
A program to check if a binary tree is BST or not
A binary search tree (BST) is a node based binary tree data structure which has the following properties.
• The left subtree of a node contains only nodes with keys less than the node’s key.
• The right subtree of a node contains only nodes with keys greater than the node’s key.
• Both the left and right subtrees must also be binary search trees.
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Tree(3)
root.left = Tree(2)
root.right = Tree(5)
root.left.left = Tree(1)
root.left.right = Tree(4)

min_max = [-1, 100]


def checkIfBST(root_node, my_array):
    if root_node is not None:
        checkIfBST(root_node.left, my_array)
        if not my_array:
            my_array.append(root_node.data)
        elif my_array[-1] < root_node.data:
            my_array.append(root_node.data)
        else:
            my_array.insert(0, 1000)
        checkIfBST(root_node.right, my_array)
        return my_array


inorder = checkIfBST(root, [])
if inorder[0] == 1000:
    print(False)
else:
    print(True)
