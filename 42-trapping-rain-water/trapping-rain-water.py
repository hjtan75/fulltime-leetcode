class Solution:
    def trap(self, height: List[int]) -> int:
    # One arrive a i, need to find element afte i which has height the same or higher than i
    # How do we know whether for x > i, is there any height[x] > height[i]
    # The brute force method would be, for every i, we look entire list to find height
    # This will TC: O(n)
    # Create an array indicating the next hightest point after i 

        if not height:
            return 0
        
        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
                
        return res
                
            
        
        

            
        
        