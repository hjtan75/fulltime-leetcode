import numpy as np
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        lager = {}
        
        for num in nums:
            if num in lager:
                lager[num] += 1
            else:
                lager[num] = 1
        
        res = [[] for i in range(len(nums) + 1)] # add one because we need the full range
        for c, v in lager.items():
            res[v].append(c)
        
        ans = []
        for i in range(len(res) - 1, 0, -1):
            ans += res[i]
            if len(ans) == k:
                return ans
        