# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Merging linked list one by one
        # This would require O(kn) where k in the number of linked list and 
        # n is the number of total element
        # The better method is that by merging a pair of linked-list
        # Every iteration, the number of linked list will device by half
        # Time complexity: O(n log k)
        
        if len(lists) == 0:
            return
          
        for i in range(len(lists) - 1):
            # Set up dummy node
            combined = ListNode()
            head = combined
            l1 = lists[0]
            l2 = lists[i+1]
            
            while l1 and l2:
                if l1.val < l2.val:
                    tmp = l1.next
                    combined.next = l1
                    l1 = tmp
                else:
                    tmp = l2.next
                    combined.next = l2
                    l2 = tmp
                combined = combined.next
            
            while l1:
                tmp = l1.next
                combined.next = l1
                l1 = tmp
                combined = combined.next
                
            while l2:
                tmp = l2.next
                combined.next = l2
                l2 = tmp
                combined = combined.next
                
            lists[0] = head.next
                    
        return lists[0]
                    
                    
                    
            
            
                    
            
