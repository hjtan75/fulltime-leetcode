# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        combined = ListNode()
        head = combined
        
        while list1 and list2:
            if list1.val < list2.val:
                tmp = list1.next
                combined.next = list1
                combined = combined.next
                list1 = tmp
            else:
                tmp = list2.next
                combined.next = list2
                combined = combined.next
                list2 = tmp
                
                # combined = combined.next
                
#             # print("L1:", list1.val, " L2:", list2.val, " Com:", combined.val)
#             t = head
#             while t != None:
#                 print(t.val, end=" ")
#                 t = t.next
                
#             print()
                
                
        while list1:
            tmp = list1.next
            combined.next = list1
            list1 = tmp
            combined = combined.next
        
        while list2:
            tmp = list2.next
            combined.next = list2
            list2 = tmp
            combined = combined.next
            
        return head.next