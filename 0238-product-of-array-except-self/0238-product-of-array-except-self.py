class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numEle = len(nums)
        ans = [1] * numEle
        prefix = 1
        postfix = 1
        
        for i in range(numEle):
            if i != numEle - 1:
                prefix *= nums[i]
                ans[i+1] *= prefix
                
        # print(ans)
        for i in range(numEle):
            if i != numEle - 1:
                postfix *= nums[numEle-i-1]
                ans[numEle-i-2] *= postfix
        
        # print(ans)
        return ans
        