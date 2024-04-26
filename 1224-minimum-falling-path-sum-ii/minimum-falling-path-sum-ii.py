class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        # use dynamic programming 
        # for the first row of dp fill it with the value from grid
        # For 2 to n - 1 row, for dp[i][j] concat the minimum value at dp[i-1][q] for all q != j
        # return the minimum on the last row
        n = len(grid)
        dp = [[0 for _ in range(n)] for _ in range(n)]
        min1_val = 10000000000
        min1_idx = 0
        min2_val = 10000000000
        min2_idx = 0
        for j in range(n):
            dp[0][j] = grid[0][j]
            if dp[0][j] < min1_val:
                    min2_val = min1_val
                    min2_idx = min1_idx
                    min1_val = dp[0][j]
                    min1_idx = j
            elif dp[0][j] < min2_val:
                min2_val = dp[0][j]
                min2_idx = j


        for i in range(1, n):
            next_min1_val = 10000000000
            next_min1_idx = 0
            next_min2_val = 10000000000
            next_min2_idx = 0
            # print(min1_val, min2_val)
            for j in range(n):
                if j != min1_idx:
                    dp[i][j] = grid[i][j] + min1_val
                else:
                    dp[i][j] = grid[i][j] + min2_val

                if dp[i][j] < next_min1_val:
                        next_min2_val = next_min1_val
                        next_min2_idx = next_min1_idx
                        next_min1_val = dp[i][j]
                        next_min1_idx = j
                elif dp[i][j] < next_min2_val:
                    next_min2_val = dp[i][j]
                    next_min2_idx = j

            min1_val = next_min1_val
            min2_val = next_min2_val
            min1_idx = next_min1_idx
            min2_idx = next_min2_idx

            

        # print(dp)
        return min(dp[n-1])

