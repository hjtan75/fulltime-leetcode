class Solution:
    def trap(self, height: List[int]) -> int:
    # One arrive a i, need to find element afte i which has height the same or higher than i
    # How do we know whether for x > i, is there any height[x] > height[i]
    # The brute force method would be, for every i, we look entire list to find height
    # This will TC: O(n)
    # Create an array indicating the next hightest point after i 

        n = len(height)
        res = 0
        idx = 0
        rMax, lMax = [0] * n, [0] * n

        cur_max = 0
        for i in range(n):
            cur_max = max(cur_max, height[i])
            lMax[i] = cur_max

        cur_max = 0
        for i in range(n-1, -1, -1):
            cur_max = max(cur_max, height[i])
            rMax[i] = cur_max

        for i in range(n):
            res += min(rMax[i], lMax[i]) - height[i]

        return res


            
        
        