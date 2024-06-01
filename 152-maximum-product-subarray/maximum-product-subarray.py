class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # The brute force method would be to find the product of every possible subarray
        # For every i, we find the product from i to j where j < n
        # Because we can find the product after by just multiplying the last element
        # TC: O(n^2), every possible subarray
        # SC: O(1)

        # Optimized method
        # We know that if the element only consist of element which are possitive
        # We maximum product is just the product of the entire array
        # We know that a negative sign would make a negative value value very large
        # Besides marking the largest product in the previous subarray,
        # we need to also store the smallest product of the previous array
        # Because it could turn very big when we encounter a negative value
        # The big problem currently is zero, anything multply by it would be zero
        # that will ruin out max and min variable
        # so when 0 is encountered, we reset the max and min to be 1, but do not considered that
        # into the the maximum product because 1 might never existed

        res = -11
        cur_max, cur_min = 1, 1

        for n in nums:
            if n == 0:
                cur_max, cur_min = 1, 1
                res = max(res, n)
                continue

            tmp = n * cur_max
            cur_max = max(n * cur_max, n * cur_min, n)
            cur_min = min(tmp, n * cur_min, n)

            res = max(res, cur_max, n)

        return res