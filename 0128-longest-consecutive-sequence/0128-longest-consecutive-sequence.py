class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        setNums = set(nums)
        maxSize = 0
        for value in nums:
            if value-1 not in setNums: # It is a starter
                size = 1
                nextValue = value + 1
                while nextValue in setNums:
                    size += 1
                    nextValue += 1
                    
                maxSize = max(size, maxSize)
                    
        return maxSize