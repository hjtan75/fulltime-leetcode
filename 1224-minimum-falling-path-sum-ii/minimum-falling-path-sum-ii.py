class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # use dynamic programming 
        # for the first row of dp fill it with the value from grid
        # For 2 to n - 1 row, for dp[i][j] concat the minimum value at dp[i-1][q] for all q != j
        # return the minimum on the last row
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        # print(n)
        for j in range(n):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            min1_val = 10000000000
            min1_idx = 0
            min2_val = 10000000000
            min2_idx = 0
            for j in range(n):
                if dp[i-1][j] < min1_val:
                    min1_val = dp[i-1][j]
                    min1_idx = j
                # if i == 3:
                #     print("-", min1_val)
            for j in range(n):
                if dp[i-1][j] < min2_val and j != min1_idx:
                    min2_val = dp[i-1][j]
                    min2_idx = j

            # print(min1_val, min2_val)
            for j in range(n):
                if j != min1_idx:
                    dp[i][j] = grid[i][j] + min1_val
                else:
                    dp[i][j] = grid[i][j] + min2_val

        # print(dp)
        return min(dp[n-1])

