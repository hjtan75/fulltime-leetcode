class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # The brute force method would be to find possible subset of the array
        # Then find that is that the half of the total sum
        # Finding every subset would require O(2^n) because for every position
        # at x, we need to consider whether to include that number

        # Our goal is to find any combination if the nums, that would made up
        # half of tthe sum of the given array
        # Using dynamic programming we can find out whether for a given index
        # could add up to the half
        # TC: O(n*sum)
        # SP: O(sum)

        summ = sum(nums)
        half = summ // 2

        if summ % 2 != 0:
            return False

        prev = [False for _ in range(half+1)]
        curr = [False for _ in range(half+1)]
        prev[0] = True

        for i in range(1, len(nums)+1):
            for j in range(half+1):
                if j - nums[i-1] >= 0:
                    curr[j] = prev[j] | prev[j - nums[i-1]]
                else:
                    curr[j] = prev[j]

            prev = curr[:]
        return curr[half]