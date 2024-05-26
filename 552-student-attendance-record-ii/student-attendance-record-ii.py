class Solution:
    def checkRecord(self, n: int) -> int:
        # the naive method would be to try out all possiblities 
        # The way to optimize is too cancel the branch when is has to possiblity to be added
        # This is a dynamic programming question
        # TC: O(3^(n-2) + )
        mod = 10**9 + 7
        dp = [[[-1 for _ in range(3)] for _ in range(2)] for _ in range(n+1)]

        # print(dp)

        def dfs(idx, absent, late):
            if absent >= 2 or late >= 3:
                return 0 

            if idx == n:
                return 1

            if dp[idx][absent][late] != -1:
                return dp[idx][absent][late]

            ans = dfs(idx+1, absent, 0)
            ans += dfs(idx+1, absent+1, 0)
            ans += dfs(idx+1, absent, late+1)

            dp[idx][absent][late] = ans % mod
            return dp[idx][absent][late]

        return dfs(0, 0, 0)