# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
sys.set_int_max_str_digits(0)
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        num = 0
        cur = head

        while cur:
            num *= 10
            num += cur.val
            cur = cur.next

        num *= 2
        num = str(num)
        cur = head
        prev = ListNode(val=-1, next=head)
       
        for n in num:
            if cur:
                cur.val = int(n)
                prev = cur
                cur = cur.next
            else:
                prev.next = ListNode(val=int(n))
                prev = prev.next

        return head



        
