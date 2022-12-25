class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # sort list with speed (n log n)
        # sustract from target starting from first elements (n/2)
        # binary search for each subtracted elements (logn)
        # Total = n log n + n/2 log n
        
        numDict = {}
        for i in range(len(nums)):
            if nums[i] in numDict:
                numDict[nums[i]].append(i)
            else:
                numDict[nums[i]] = [i]
        
        for num in nums:
            sub = target - num
            if sub in numDict:
                if sub == num:
                    if len(numDict[sub]) > 1:
                        return [numDict[sub][0], numDict[sub][1]]
                else:
                    return [numDict[num][0], numDict[sub][0]]