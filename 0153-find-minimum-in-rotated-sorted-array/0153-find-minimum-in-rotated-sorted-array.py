class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        
        if len(nums) <= 2:
            return min(nums)
        
        # No rotation
        if nums[0] < nums[-1]:
            return nums[0]
        
        while l <= r:
            m = ceil((l + r)/2)
            if nums[m] < nums[m - 1]:
                return nums[m]
            
            if nums[m] < nums[0]:
                r = m - 1
            else:
                l = m + 1
                
        return 0
            