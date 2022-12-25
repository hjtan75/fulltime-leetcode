class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numEle = len(nums)
        ans = [1] * numEle
        prefix = 1
        postfix = 1
        
        for i in range(numEle):
            if i != numEle - 1:
                prefix *= nums[i]
                postfix *= nums[numEle-i-1]
                ans[i+1] *= prefix
                ans[numEle-i-2] *= postfix
                
        return ans
        