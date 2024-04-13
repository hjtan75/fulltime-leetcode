class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        # Calculate the maximum rectangular on every row 
        # Calculate the maximum rectangular with monotonic stack
        # TC: O(row * col)

        row, col = len(matrix), len(matrix[0])
        max_rect = 0
        height = [0]*(col+1)

        for row in matrix:
            for i in range(col):
                if row[i] == '1':
                    height[i] += 1
                else:
                    height[i] = 0

            stack = []
            for i in range(len(height)):
                
                while stack and height[i] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_rect = max(max_rect, h*w)
                stack.append(i)

        return max_rect