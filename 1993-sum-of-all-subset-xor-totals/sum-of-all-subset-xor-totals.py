class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        self.len_nums = len(nums)
        self.res = 0


        def dfs(curr_loc, current_list):
            if curr_loc >= self.len_nums:
                ans = 0
                for num in current_list:
                    ans ^= num
                self.res += ans
                return

            current_list.append(nums[curr_loc])
            dfs(curr_loc+1, current_list)
            current_list.pop()
            dfs(curr_loc+1, current_list)


        dfs(0, [])
        return self.res


