class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        numEle = len(nums)
        prefix = [0] * numEle
        postfix = [0] * numEle
        ans = [0] * numEle
        
        for i in range(numEle):
            if i == 0:
                prefix[i] = nums[i]
                postfix[numEle-i-1] = nums[numEle-i-1]
            else:
                prefix[i] = nums[i] * prefix[i-1]
                postfix[numEle-i-1] = nums[numEle-i-1] * postfix[numEle-i]
                
        # print(postfix)
        # print(prefix)
        for i in range(numEle):
            if i == 0:
                ans[i] = postfix[i+1]
            elif i == numEle - 1:
                ans[i] = prefix[i-1]
            else:
                ans[i] = postfix[i+1] * prefix[i-1]
                
        # print(ans)
        return ans
        