# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_sum = 0
        curr_node = head.next
        start_ptr = head

        while curr_node != None:
            if curr_node.val == 0:
                start_ptr.val = curr_sum
                start_ptr.next = curr_node
                curr_sum = 0
                if curr_node.next != None:
                    start_ptr = curr_node
                else:
                    start_ptr.next = None
            else:
                curr_sum += curr_node.val
            curr_node = curr_node.next

        return head
        