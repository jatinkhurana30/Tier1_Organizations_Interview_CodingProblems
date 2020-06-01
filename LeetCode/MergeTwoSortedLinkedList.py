"""Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4"""


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        finalList = None
        l1_node = l1
        l2_node = l2
        final_list_counter = finalList

        while l1_node is not None and l2_node is not None:
            if l1_node.val <= l2_node.val:
                # add l1_node to final node
                if finalList is None:
                    finalList = ListNode(l1_node.val)
                    final_list_counter = finalList
                else:
                    final_list_counter.next = ListNode(l1_node.val)
                    final_list_counter = final_list_counter.next
                l1_node = l1_node.next
            elif l1_node.val > l2_node.val:
                # add l2 to final list
                if finalList is None:
                    finalList = ListNode(l2_node.val)
                    final_list_counter = finalList
                else:
                    final_list_counter.next = ListNode(l2_node.val)
                    final_list_counter = final_list_counter.next
                l2_node = l2_node.next

        if l1_node is not None:
            while l1_node is not None:
                # add l1 to final list
                if finalList is None:
                    finalList = ListNode(l1_node.val)
                    final_list_counter = finalList
                else:
                    final_list_counter.next = ListNode(l1_node.val)
                    final_list_counter = final_list_counter.next
                l1_node = l1_node.next

        if l2_node is not None:
            while l2_node is not None:
                # add l1 to final list
                if finalList is None:
                    finalList = ListNode(l2_node.val)
                    final_list_counter = finalList
                else:
                    final_list_counter.next = ListNode(l2_node.val)
                    final_list_counter = final_list_counter.next
                l2_node = l2_node.next

        return finalList

    def addToFinalList(self, node_val, finalList, final_list_counter):
        if finalList is None:
            finalList = ListNode(node_val)
            final_list_counter = finalList
        else:
            final_list_counter.next = ListNode(node_val)
            final_list_counter = final_list_counter.next

        return finalList, final_list_counter








