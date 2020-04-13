"""Find the closest element in Binary Search Tree Given a binary search tree and a target node K. The task is to find
the node with minimum absolute difference with given target value K.

https://www.geeksforgeeks.org/find-closest-element-binary-search-tree/

// For above binary search tree
Input  :  k = 4
Output :  4

Input  :  k = 18
Output :  17

Input  :  k = 12
Output :  9

"""


class BST:
    def __init__(self, data):
        self.data = data
        self.left_node = None
        self.right_node = None


# Driver Code to construct BST
root_node = BST(9)
root_node.left_node = BST(4)
root_node.right_node = BST(17)
root_node.left_node.left_node = BST(3)
root_node.left_node.right_node = BST(6)
root_node.right_node.right_node = BST(22)
root_node.left_node.right_node.left_node = BST(5)
root_node.left_node.right_node.right_node = BST(7)
root_node.right_node.right_node.left_node = BST(20)


def find_closest_element(root, X):
    if root.data == X:
        return root.data
    elif root.data < X:
        current_difference = X - root.data
        if root.right_node is not None:
            next_elem = find_closest_element(root.right_node, X)
        else:
            return root.data
        if next_elem - X < current_difference:
            return next_elem
        else:
            return root.data
    elif root.data > X:
        current_difference = root.data - X
        if root.left_node is not None:
            next_elem = find_closest_element(root.left_node, X)
        else:
            return root.data
        if X - next_elem < current_difference:
            return next_elem
        else:
            return root.data


print(find_closest_element(root_node, 10))
