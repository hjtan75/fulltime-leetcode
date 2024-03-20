# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the reference for a and b
        # Relocate refernce for b-1 to list2, and the end of list2 to b
        # Edge cases, when a = 0, b = n, a = b
        # Time complexity: O(n)

        head = ListNode(0, list1)
        a_prev_ptr, b_aft_ptr = head, list1
        list2_end = list2

       
        while a_prev_ptr and a > 0:
            a_prev_ptr = a_prev_ptr.next
            a -= 1

        while b_aft_ptr and b >= 0:
            b_aft_ptr = b_aft_ptr.next
            b -= 1

        while list2_end.next:
            list2_end = list2_end.next

        a_prev_ptr.next = list2
        list2_end.next = b_aft_ptr
        return head.next