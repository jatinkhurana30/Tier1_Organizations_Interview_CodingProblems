"""
Write a program to find the node at which the intersection of two singly linked lists begins.

For example, the following two linked lists:


begin to intersect at node c1.



Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
Output: Reference of the node with value = 8
Input Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,0,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.


Example 2:


Input: intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Reference of the node with value = 2
Input Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect). From the head of A, it reads as [0,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.


Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: null
Input Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.


Notes:

If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
Your code should preferably run in O(n) time and use only O(1) memory.
"""

"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:

        lengthA = 0
        lengthB = 0
        current_nodeA = headA
        current_nodeB = headB
        while current_nodeA is not None:
            lengthA += 1
            current_nodeA = current_nodeA.next

        while current_nodeA is not None:
            lengthB += 1
            current_nodeB = current_nodeB.next

        extra_nodes = None
        n = 0
        compareWith = None
        if lengthA < lengthB:
            extra_nodes = headB
            n = lengthB - lengthA
            compareWith = headA
        else:
            extra_nodes = headA
            n = lengthA - lengthB
            compareWith = headB

        for i in range(0, n):
            if hash(extra_nodes) == hash(compareWith):
                return extra_nodes
            extra_nodes = extra_nodes.next

        current_nodeA = compareWith
        current_nodeB = extra_nodes

        while current_nodeA is not None and current_nodeB is not None:
            if hash(current_nodeA) == hash(current_nodeB):
                return current_nodeA
            else:
                current_nodeA = current_nodeA.next
                current_nodeB = current_nodeB.next
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        my_map = {}

        current_nodeA = headA
        current_nodeB = headB

        while current_nodeA is not None:
            my_map[current_nodeA] = 1
            current_nodeA = current_nodeA.next

        while current_nodeB is not None:
            if current_nodeB in my_map:
                return current_nodeB
            current_nodeB = current_nodeB.next

