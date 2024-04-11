class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        # We check position i and i+1
        # If i > i+1, remove i, else advance
        # If i reach end of string but k > 0
        # Pop number from the back
        # TC: O(n), parsing through every element in num
        # MC: O(n), res

        stack = []

        for n in num:
            while stack and k > 0 and stack[-1] > n:
                stack.pop()
                k -= 1
            stack.append(n)

        if k > 0:
            stack = stack[:-k]

        res = ''.join(stack).lstrip('0')
        if res:
            return res
        else:
            return '0'
            