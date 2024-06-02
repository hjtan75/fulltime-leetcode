class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The brute force approach would be to sum all the possible subarray
        # This will take O(n^2) time

        # At every cell could make a decision, it could be added to the previous array
        # Or the start from the cell. WE make this decision by each value
        # Then in every iteration, we compare to the maximum
        # TC: O(n)
        # SC: O(1)

        cur_max = nums[0]
        res = nums[0]
        n = len(nums)

        for i in range(1, n):
            if nums[i] > nums[i] + cur_max:
                cur_max = nums[i]
            else:
                cur_max += nums[i]

            res = max(cur_max, res)

        return res
        