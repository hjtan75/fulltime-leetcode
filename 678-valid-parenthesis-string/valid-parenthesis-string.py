class Solution:
    def checkValidString(self, s: str) -> bool:
        # Create a stack that loads ( and *
        # if ) is encountered, try to find the the ( in the stack, if not use *
        # If empty stack return false
        # If stack only contain * in the end return true, else return false

        stack = []

        for c in s:
            if c == '(' or c == '*':
                stack.append(c)
            else:
                if not stack:
                    return False
                
                nearest_left = -1
                for i in range(len(stack)-1, -1, -1):
                    if stack[i] == '(':
                        nearest_left = i
                        break
                
                if nearest_left != -1:
                    stack = stack[:nearest_left] + stack[nearest_left+1:]
                else:
                    stack.pop()

        print(stack)
        if len(stack) == 0:
            return True
        else:
            left_count = 0
            for c in stack:
                if c != '*':
                    left_count += 1
                else:
                    if left_count > 0:
                        left_count -= 1
            if left_count > 0:
                return False
            else:
                return True

     