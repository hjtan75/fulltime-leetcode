class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if c in '([{':
                stack.append(c)
            if c == ")" and (len(stack) == 0 or stack.pop() != '('):
                return False
            if c == "]" and (len(stack) == 0 or stack.pop() != '['):
                return False
            if c == "}" and (len(stack) == 0 or stack.pop() != '{'):
                return False

        if len(stack) > 0:
            return False
        return True