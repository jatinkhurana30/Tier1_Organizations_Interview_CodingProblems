"""Construct BST from given preorder traversal | Set 1
Given preorder traversal of a binary search tree, construct the BST.

For example, if the given traversal is {10, 5, 1, 7, 40, 50}, then the output should be root of following tree.
https://www.geeksforgeeks.org/construct-bst-from-given-preorder-traversa/
"""


class Tree:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None


input_list = list(map(int, input().split(', ')))


def generate_tree(tree, pre_list):
    if len(pre_list) == 0:
        return tree

    tree = Tree(pre_list.pop(0))

    if len(pre_list) == 0:
        return tree

    for i in range(0, len(pre_list)):
        if pre_list[i] >= tree.data:
            left_nodes = pre_list[0:i]
            right_nodes = pre_list[i:]
            break
    tree.left = generate_tree(tree.left, left_nodes)
    tree.right = generate_tree(tree.right, right_nodes)
    return tree


my_tree = generate_tree("", input_list)


def print_inorder(root):
    if root is None:
        return

    print_inorder(root.left)
    print(root.data)
    print_inorder(root.right)


print(print_inorder(my_tree))
