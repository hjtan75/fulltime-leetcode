import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lager = {}
        
        for num in nums:
            if num in lager:
                lager[num] += 1
            else:
                lager[num] = 1
        
        # print(lager)
        sorted_dict = sorted(lager.items(), key=lambda x: x[1], reverse=True)
        
        # print(sorted_dict)
        
        ans = []
        for i in range(k):
            ans.append(sorted_dict[i][0])
        return ans