"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldPtr = head
        newHead = None
        preNode = None
        valArr = []
        dictPtr = {}

        numNode = 0
        while oldPtr != None:
            newNode = Node(oldPtr.val, None, None)
            dictPtr[oldPtr] = newNode

            if numNode == 0:
                newHead = newNode
            else:
                preNode.next = newNode
            numNode += 1
            oldPtr = oldPtr.next
            preNode = newNode

        oldPtr = head
        newPtr = newHead
        while oldPtr != None:
            if oldPtr.random != None:
                newPtr.random = dictPtr[oldPtr.random]
            oldPtr = oldPtr.next
            newPtr = newPtr.next

        return newHead

            