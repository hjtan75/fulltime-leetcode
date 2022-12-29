class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The naive method is with a 3 layer loop O(n^3)
        # We must first sort the array to elimited using the same elements
        # Prevent using the same element with sets
        # First term is for sorting the array, second term is the two layer loop
        # One for iterate through all first element, second is for iterate two sum
        # Time complexity: O(nlogn) + O(n^2)
        # Memory complexity: O(n)
        
        ans = []
        nums.sort()
        
        for fIdx in range(len(nums)-2):
            if fIdx == 0 or nums[fIdx] != nums[fIdx-1]:
                sIdx = fIdx + 1
                tIdx = len(nums) - 1
                
                while sIdx < tIdx:
                    threeSum = nums[fIdx] + nums[sIdx] + nums[tIdx]
                    if sIdx - 1 != fIdx and nums[sIdx] == nums[sIdx-1]:
                        sIdx += 1
                    else:
                        if threeSum == 0:
                            ans.append([nums[fIdx], nums[sIdx], nums[tIdx]])
                            sIdx += 1
                            tIdx -= 1
                        elif threeSum > 0:
                            tIdx -= 1
                        else:
                            sIdx += 1    
        return ans
                        
                    
                
                
        
                    
        