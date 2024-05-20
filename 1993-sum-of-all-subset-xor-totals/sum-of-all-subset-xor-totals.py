class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.len_nums = len(nums)
        self.res = 0


        def dfs(curr_loc, res):
            if curr_loc >= self.len_nums:
                return res

            include = dfs(curr_loc+1, res ^ nums[curr_loc])
            exclude = dfs(curr_loc+1, res)
            return include + exclude

        
        return dfs(0, 0)


