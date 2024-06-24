class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # The brute force method would be to find possible subset of the array
        # Then find that is that the half of the total sum
        # Finding every subset would require O(2^n) because for every position
        # at x, we need to consider whether to include that number

        # If we use memoization, if will cut the time down to only O(n)
        # We create an array with size n*2, the first dimension is that we didn't choose the 
        # element, the second element meant that we chose the element

        # Edge case where the sum can't divide by two
        if sum(nums) % 2 != 0:
            return False

        # Create a dp array with row as summ and i as index
        half = sum(nums) // 2
        dp = [[False for _ in range(half+1)] for _ in range(len(nums)+1)]

        dp[0][0] = True
        # print(dp)
        for i in range(1, len(nums)+1):
            for j in range(half+1):
                # print(i, j)
                if j - nums[i-1] >= 0:
                    dp[i][j] = dp[i-1][j] | dp[i-1][j-nums[i-1]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[len(nums)][half]
