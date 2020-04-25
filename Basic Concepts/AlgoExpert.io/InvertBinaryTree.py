"""
Mirror of a Tree: Mirror of a Binary Tree T is another Binary Tree M(T) with left and right children of all non-leaf nodes interchanged.

https://www.geeksforgeeks.org/write-an-efficient-c-function-to-convert-a-tree-into-its-mirror-tree/
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


root = Tree(1)
root.left = Tree(3)
root.right = Tree(2)
root.right.left = Tree(5)
root.right.right = Tree(4)


def mirror_my_tree(root_node):
    if root is None:
        return

    root_node.left, root_node.right = root_node.right, root_node.left
    if root_node.left is not None: mirror_my_tree(root_node.left)
    if root_node.right is not None: mirror_my_tree(root_node.right)
    return root_node


def inorder_traversal(root_node):
    if root_node is None:
        return
    inorder_traversal(root_node.left)
    print(root_node.data, end=' ')
    inorder_traversal(root_node.right)


inorder_traversal(root)
print('')
root = mirror_my_tree(root)
inorder_traversal(root)

