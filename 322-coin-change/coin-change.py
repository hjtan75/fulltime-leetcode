class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0:0}

        for i in coins:
            dp[i] = 1

        def dfs(leftover):
            if leftover in dp:
                return dp[leftover]

            if leftover < 0:
                return -1

            res = 2**31 - 1
            for coin in coins:
                ways = dfs(leftover-coin)
                if ways != -1:
                    res = min(ways, res)
            res += 1

            if res < 2**31 - 1:
                dp[leftover] = res
                return res
            else:
                dp[leftover] = -1
                return -1

        return dfs(amount)