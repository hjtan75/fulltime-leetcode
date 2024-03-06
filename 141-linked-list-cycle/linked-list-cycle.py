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
        # WHen the slow ptr enter the loop, no matter where the fast ptr is
        # The fast pointer will be one place close to the slow pointer
        # If the difference is distance is 3, the fast ptr will catch to the slow ptr in three iteration
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
