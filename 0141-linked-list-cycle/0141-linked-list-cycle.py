# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        node = head
        visited = set()
        position = 0
        
        
        while node != None:
            if node in visited:
                return True
            else:
                visited.add(node)
                
            node = node.next
        
        return False