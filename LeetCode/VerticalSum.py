class Tree:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def getHorizontalDistances(root_node):
    my_map = {}
    my_map = getHorizontalDistance(root_node, 0, my_map)
    return my_map


def getHorizontalDistance(root_node, d, my_map):

    if root_node is None:
        return my_map

    if d in my_map:
        my_map[d].append(root_node.val)
    else:
        my_map[d] = [root_node.val]

    # my_map[root_node.val] = d
    getHorizontalDistance(root_node.left, d-1, my_map)
    getHorizontalDistance(root_node.right, d + 1, my_map)
    return my_map


root = Tree(5)
root.left = Tree(10)
root.right = Tree(12)
root.right.left = Tree(1)
root.right.right = Tree(9)
root.left.left = Tree(6)
root.left.right = Tree(7)

print(getHorizontalDistances(root))