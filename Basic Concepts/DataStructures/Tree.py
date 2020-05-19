class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
            return True

        current_node = self.root
        while True:
            if data < current_node.data:
                if current_node.left is None:
                    current_node.left = TreeNode(data)
                    return True
                current_node = current_node.left
            elif data >= current_node.data:
                if current_node.right is None:
                    current_node.right = TreeNode(data)
                    return True
                current_node = current_node.right
        return False


my_tree = BinaryTree()

my_tree.insert(5)
my_tree.insert(6)
my_tree.insert(8)

