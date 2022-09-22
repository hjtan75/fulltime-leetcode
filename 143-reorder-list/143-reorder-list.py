# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        
        # Use two pointer to find the mid point
        # Reverse the lower half of the array
        slow = head
        fast = head.next
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
            
        cur, pre, nex = slow.next, None, None
        slow.next = None
        while cur != None:
            nex = cur.next
            cur.next = pre
            pre = cur
            cur = nex
        
        
        # Combine the 2 list
#         firstList = head
#         secondList = pre
        
#         while secondList:
#             tmp1 = firstList.next
#             tmp2 = secondList.next
#             firstList.next = secondList
#             secondList.next = tmp1
#             firstList, secondList = tmp1, tmp2

        firstList = head.next
        secondList = pre
        combinedList = head
        noNode = 1
        
        while firstList or secondList:
            if noNode % 2 == 0:
                tmp = firstList
                combinedList.next = firstList
                combinedList = combinedList.next
                firstList = tmp.next
            else:
                tmp = secondList
                combinedList.next = secondList
                combinedList = combinedList.next
                secondList = tmp.next
            noNode += 1
            
        while firstList:
            tmp = firstList
            combinedList.next = firstList
            combinedList = combinedList.next
            firstList = tmp.next
            
            
            
                
        
        
        
        
        
            
            