# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        slow, fast = head, head
        # Fast is n node ahead of slow
        for i in range(n):
            fast = fast.next
        if not fast:
            if head.next:
                head = head.next
                return head
            else:
                return None
        # Traverse until fast is the last element
        while fast.next:
            fast = fast.next
            slow = slow.next

        if slow.next and slow.next.next:
            slow.next = slow.next.next
        else:
            slow.next = None

        return head

