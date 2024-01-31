class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Create a monotonic stack
        # Where the element in the stack is non-increasing
        # Each element contained two element [val, idx]
        # When a smaller value encountered, added to the stack
        # when a larger value encountered, pop from stack and fill the pop index
        # until the top of stack is larger than the encountered item
        # Time complexity: O(n) each item has to be added and popped to and from the stack

        stack = []
        res = [0] * len(temperatures)

        for idx, val in enumerate(temperatures):
            if len(stack) == 0 or stack[-1][0] >= val:
                stack.append([val, idx])
            else:
                while len(stack) != 0 and val > stack[-1][0]:
                    new_val, new_idx = stack.pop()
                    res[new_idx] = idx - new_idx
                    
                stack.append([val, idx])

        return res