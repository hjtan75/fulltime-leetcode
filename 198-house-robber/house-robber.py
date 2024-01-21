class Solution:
    def rob(self, nums: List[int]) -> int:
        # This is a dynamic programming question
        # For every house, we can choose from either the i-2 or i-3 house to choose from
        # For the last iteration, there are two houses to choose from
        # return the maximum one
        # Settle edge cases

        if len(nums) <= 2:
            return max(nums)

        c1, c2, c3 = nums[0], nums[1], nums[0] + nums[2]
        num_houses = len(nums)

        for i in range(3, num_houses):
            c1, c2, c3 = c2, c3, max(c1, c2) + nums[i]


        return max(c2, c3)

        