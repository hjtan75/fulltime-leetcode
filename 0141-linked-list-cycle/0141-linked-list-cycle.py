# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = head
        f = head
        
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        
        return False