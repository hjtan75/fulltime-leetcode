# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # Traditional method would use a set to keep track of the visited node
        # But it need O(n) memory complexity
        # We can reduce it to O(1) with the fast-slow pointer method
        # The idea is if there exist a loop, the fast pointer will 
        # meet the slow pointer at some point other than the starting position
        # This is true because every iteration, the fast pointer increase 2 steps
        # the slow pointer increase 1 steps, this means that the gap between both
        # pointer decrease by 1 step.
        # Thus they will eventually meet
        # Time complexity: O(n)
        # Memory complexity: O(1)
        
        s = head
        f = head
        
        while f != None and f.next != None:
            f = f.next.next
            s = s.next
            if s == f:
                return True
        
        return False