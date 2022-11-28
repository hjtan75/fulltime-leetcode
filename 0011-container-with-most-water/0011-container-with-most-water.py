class Solution:
    def maxArea(self, height: List[int]) -> int:
        left_ptr = 0
        right_ptr = len(height) - 1
        max_vol = 0
        
        while left_ptr < right_ptr:
            vol = min(height[left_ptr], height[right_ptr]) * (right_ptr - left_ptr)
            if vol > max_vol:
                max_vol = vol
                
            if height[left_ptr] > height[right_ptr]:
                right_ptr -= 1
            else:
                left_ptr += 1
                
        return max_vol