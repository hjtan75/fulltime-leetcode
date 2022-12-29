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
        sortedNums = sorted(nums)
        
        for fIdx in range(len(sortedNums)-2):
            if fIdx == 0 or sortedNums[fIdx] != sortedNums[fIdx-1]:
                sIdx = fIdx + 1
                tIdx = len(sortedNums) - 1
                
                while sIdx < tIdx:
                    threeSum = sortedNums[fIdx] + sortedNums[sIdx] + sortedNums[tIdx]
                    if sIdx - 1 != fIdx and sortedNums[sIdx] == sortedNums[sIdx-1]:
                        sIdx += 1
                    else:
                        if threeSum == 0:
                            ans.append([sortedNums[fIdx], sortedNums[sIdx], sortedNums[tIdx]])
                            # usedNums2.add(sortedNums[sIdx])
                            sIdx += 1
                            tIdx -= 1
                        elif threeSum > 0:
                            tIdx -= 1
                        else:
                            sIdx += 1    
                
                # usedNums.add(sortedNums[fIdx])
        return ans
                        
                    
                
                
        
                    
        