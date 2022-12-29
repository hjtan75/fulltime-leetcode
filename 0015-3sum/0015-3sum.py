class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # The naive method is with a 3 layer loop O(n^3)
        # We must first sort the array to elimited using the same elements
        # Prevent using the same element with sets
        
        usedNums = set()
        ans = []
        sortedNums = sorted(nums)
        
        for fIdx in range(len(sortedNums)-2):
            if sortedNums[fIdx] not in usedNums:
                sIdx = fIdx + 1
                tIdx = len(sortedNums) - 1
                usedNums2 = set()
                
                while sIdx < tIdx:
                    threeSum = sortedNums[fIdx] + sortedNums[sIdx] + sortedNums[tIdx]
                    if sortedNums[sIdx] in usedNums2:
                        sIdx += 1
                    else:
                        if threeSum == 0:
                            ans.append([sortedNums[fIdx], sortedNums[sIdx], sortedNums[tIdx]])
                            usedNums2.add(sortedNums[sIdx])
                            sIdx += 1
                            tIdx -= 1
                        elif threeSum > 0:
                            tIdx -= 1
                        else:
                            sIdx += 1    
                
                usedNums.add(sortedNums[fIdx])
        return ans
                        
                    
                
                
        
                    
        