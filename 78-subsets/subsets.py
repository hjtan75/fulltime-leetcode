class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # O(n**2) - Number of subset
        # O(n) - Adding element to each subset
        res = []

        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                return

            subset.append(nums[i])
            dfs(i+1)
            subset.pop()
            dfs(i+1)

        dfs(0)
        return res


