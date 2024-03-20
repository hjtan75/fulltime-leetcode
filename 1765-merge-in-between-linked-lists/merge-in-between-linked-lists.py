# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        # Find the reference for a and b
        # Relocate refernce for b-1 to list2, and the end of list2 to b
        # Edge cases, when a = 0, b = n, a = b, not a = 0 or b = 0
        # Time complexity: O(n)

        ptr1 = list1
        for _ in range(a-1):
            ptr1 = ptr1.next

        ptr2 = ptr1.next
        for _ in range(b-a+1):
            ptr2 = ptr2.next

        ptr1.next = list2
        while list2.next:
            list2 = list2.next
        list2.next = ptr2
        return list1