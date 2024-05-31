# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # because we could get the parent of the deleted node
        # we could only change the value of the current node to the next node
        # then delete the last node
        node.val = node.next.val
        node.next = node.next.next


        