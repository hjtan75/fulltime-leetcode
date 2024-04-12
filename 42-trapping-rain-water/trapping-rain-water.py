class Solution:
    def trap(self, height: List[int]) -> int:
        # There are two solution, both require TC: O(n)
        # First soluion: MC: O(n)
        # Create two array, each indicating the maximum height from the left and right
        # Find the minumum between two direction and subtract the current height

        # Second solution: MC: O(1)
        # Create two pointer indicate the left and the maximum height
        # If leftMax > rightMax, meaning that for i which rightMax - 1 is always bound by the rightMax
        # So set water of rightMax - 1 = rightMax - height[i]
        # Vice versa

        l, r = 0, len(height) - 1
        res, maxLeft, maxRight = 0, height[l], height[r]

        while l < r:
            if maxLeft < maxRight:
                l += 1
                maxLeft = max(maxLeft, height[l])
                res += maxLeft - height[l]
            else:
                r -= 1
                maxRight = max(maxRight, height[r])
                res += maxRight - height[r]

        return res
            
        
        

            
        
        