class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        com = []
        def backtracking(idx):
            if idx == len(nums):
                res.append(com.copy())
                return

            com.append(nums[idx])
            backtracking(idx+1)
            prev = com.pop()
            while idx + 1 < len(nums) and nums[idx + 1] == prev:
                idx += 1
            backtracking(idx+1)

        backtracking(0)
        return res
            