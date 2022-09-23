# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer method
        # Distane between the two pointer will always be n
        dummy = ListNode(0, head)
        left = dummy
        right = head
        
        # Shifting the right pointer
        while n > 0:
            right = right.next
            n -= 1
        
        # Shifting both pointer
        while right:
            right = right.next
            left = left.next
            
        # Delete 
        left.next = left.next.next
        return dummy.next