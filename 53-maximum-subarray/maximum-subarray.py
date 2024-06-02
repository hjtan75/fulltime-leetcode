class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # The brute force approach would be to sum all the possible subarray
        # This will take O(n^2) time

        # At every cell could make a decision, it could be added to the previous array
        # Or the start from the cell. WE make this decision by each value
        # Then in every iteration, we compare to the maximum

        cur_max = -1000000001
        res = -1000000001

        for n in nums:
            if n > n + cur_max:
                cur_max = n
            else:
                cur_max += n

            res = max(cur_max, res, n)

        return res
        