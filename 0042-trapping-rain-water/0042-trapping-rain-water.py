class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = [0]
        maxR = [0]
        vol = 0
        
        for i in range(1, len(height)):
            maxL.append(max(maxL[-1], height[i-1]))
            maxR.insert(0, max(maxR[0], height[len(height) - i]))
            
        # print(maxL)
        # print(maxR)
        
        for i in range(len(height)):
            v = min(maxL[i], maxR[i]) - height[i]
            # print(v)
            if v > 0:
                vol += v
                
        return vol
            
        
        