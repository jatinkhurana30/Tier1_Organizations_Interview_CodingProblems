"""
A linked list is given such that each node contains an additional random pointer which could point to any node in the list or null.

Return a deep copy of the list.

The Linked List is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

val: an integer representing Node.val
random_index: the index of the node (range from 0 to n-1) where random pointer points to, or null if it does not point to any node.


Example 1:


Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
Example 2:


Input: head = [[1,1],[2,1]]
Output: [[1,1],[2,1]]
Example 3:



Input: head = [[3,null],[3,0],[3,null]]
Output: [[3,null],[3,0],[3,null]]
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None

        length_map = {}
        l = 0
        length_map[head] = 0
        current_node = head.next

        new_head = Node(head.val)
        new_current_node = new_head

        while current_node is not None:
            l = l + 1
            new_node = Node(current_node.val)
            new_current_node.next = new_node
            new_current_node = new_current_node.next
            length_map[current_node] = l
            current_node = current_node.next

        current_node = head
        new_current_node = new_head
        while current_node is not None:
            random_node = current_node.random
            if random_node is not None:
                length_of_random = length_map[random_node]
                self.set_random(new_head, new_current_node, length_of_random)
            new_current_node = new_current_node.next
            current_node = current_node.next

        return new_head

    def set_random(self, head, current, node_count):
        current_node = head
        l = 0
        while current_node is not None:
            if l == node_count:
                current.random = current_node
                return None
            l += 1
            current_node = current_node.next





