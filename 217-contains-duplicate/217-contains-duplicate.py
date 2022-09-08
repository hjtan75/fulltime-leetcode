class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ss = set(nums);
        
        if len(ss) == len(nums):
            return False
        else:
            return True
            