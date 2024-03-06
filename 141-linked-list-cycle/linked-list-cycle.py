# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # There is a solution where two pointer is used
        # One fast pointer and the other one is slow
        # If the fast pointer meet the slow pointer, there is a loop
        # If the fast pointer reachers the end before meeting the slow pointer
        # There is not loop
        # Time: O()
        # Memory: O(1)
        if head == None or head.next == None:
            return False

        slow, fast = head, head.next

        while fast.next and fast.next.next:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next

        return False
