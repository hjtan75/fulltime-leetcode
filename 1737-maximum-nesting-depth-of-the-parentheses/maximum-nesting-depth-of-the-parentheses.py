class Solution:
    def maxDepth(self, s: str) -> int:
        # Use a variable to keep track of number of left paranthesis
        # This variable indicate depth
        # Then record the maximum depth by checking the length of stack
        # If the right paranthesis is received, decrement variable

        depth, max_depth = 0, 0

        for c in s:
            if c == '(':
                depth += 1
                max_depth = max(max_depth, depth)
            elif c == ')':
                depth -= 1

        return max_depth


        