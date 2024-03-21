# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we need to set three set of pointers
        # And reverse the pointer one by one
        # Edge cases: number of node < 3
        # O(n): Time complexity, parsing every node once
        # O(1): Mem complexity, only use two pointer

        if head == None or head.next == None:
            return head
        if head.next.next == None:
            end = head.next
            end.next = head
            head.next = None
            return end


        ptr1, ptr2, ptr3 = head, head.next, head.next.next
        head.next = None

        while ptr3:
            print(ptr3.val)
            ptr2.next = ptr1
            ptr1 = ptr2
            ptr2 = ptr3
            ptr3 = ptr3.next
            

        ptr2.next = ptr1
        return ptr2
        