class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (index, height)
        # We want to keep the monotonicly increase stack based on height
        largestArea = 0
        stack = []
        
        for i in range(len(heights)):
            if not stack or heights[i] >= stack[-1][1]:
                stack.append((i, heights[i]))
            else:
                
                lastPoppedIndex = -1
                while stack and heights[i] < stack[-1][1]:
                    area =  (i - stack[-1][0]) * stack[-1][1]
                    largestArea = max(area, largestArea)
                    lastPoppedIndex = stack[-1][0]
                    stack.pop()
                stack.append((lastPoppedIndex, heights[i]))
            
        for i, h in stack[::-1]:
            area = (len(heights) - i) * h
            largestArea = max(area, largestArea)
            
        return largestArea
            
            
            
                