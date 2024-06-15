class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # The intuition is to use a stack to mark idx of open paranthesis
        # When we sees a close paranthesis, when stack is empty, pop from stack
        # if not remove the close paranthesis
        # If finish iterating all of s, delete all remainding open paranthesis in the element
        # TC: O(n) iterate through the array
        # SP: O(n) for the stack

        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append(i)
                i += 1
            elif s[i] == ')':
                if len(stack) == 0:
                    s = s[:i] + s[i+1:]
                else:
                    stack.pop()
                    i += 1
            else:
                i += 1
        
        for i in range(len(stack)-1, -1, -1):
            s = s[:stack[i]] + s[stack[i]+1:]

        return s
