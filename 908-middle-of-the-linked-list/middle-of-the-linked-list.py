# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Using a fast ptr and a slow pointer
        # We can find out the middle point when the fast pointer reach the end
        # Time complexity: O(n / 2)
        # Memory complexity: O(1)

        fast, slow = head, head

        while fast.next and fast.next.next:
            fast = fast.next.next
            slow = slow.next

        if fast.next:
            return slow.next
        else:
            return slow
