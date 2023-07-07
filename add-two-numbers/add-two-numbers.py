# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1 = l1
        cur2 = l2
        ans = ListNode()
        ansPtr = ans
        carry = 0

        while cur1 and cur2:
            sum = carry + cur1.val + cur2.val
            n = ListNode(sum % 10)
            carry = sum // 10
            ansPtr.next = n
            ansPtr = ansPtr.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            sum = carry + cur1.val
            n = ListNode(sum % 10)
            carry = sum // 10
            ansPtr.next = n
            ansPtr = ansPtr.next
            cur1 = cur1.next

        while cur2:
            sum = carry + cur2.val
            n = ListNode(sum % 10)
            carry = sum // 10
            ansPtr.next = n
            ansPtr = ansPtr.next
            cur2 = cur2.next

        if carry > 0:
            n = ListNode(carry)
            ansPtr.next = n

        return ans.next

