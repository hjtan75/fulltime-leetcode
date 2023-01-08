class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lowestPoint = self.findingLowest(nums)
        newArr = nums[lowestPoint:] + nums[:lowestPoint]
        # print(lowestPoint)
        # print(newArr)
        l = 0
        r = len(newArr) - 1
        
        while l <= r:
            m = ceil((l+r)/2)
            if newArr[m] == target:
                return (m+lowestPoint)%len(nums)
            elif newArr[m] > target:
                r = m - 1
            else:
                l = m + 1
        
        return -1
    def findingLowest(self, nums):
        if nums[0] < nums[-1]:
            return 0
        else:
            l = 0
            r = len(nums) - 1
            
            while l <= r:
                m = ceil((l+r)/2)
                
                if nums[m] < nums[m-1]:
                    lowestPoint = m
                    return m
                    
                if nums[m] > nums[0]:
                    l = m + 1
                else:
                    r = m - 1
        return -1
