# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # We can use reversing the stack, but it's very troublesome
        # The other method we can use recursive, returning any carry to the previous node

        def double_num(node):
            if not node:
                return 0

            digit = (node.val * 2) + double_num(node.next)
            node.val = digit % 10
            return digit // 10

        carry = double_num(head)
        if carry > 0:
            return ListNode(val=carry, next=head)
        else:
            return head



        
