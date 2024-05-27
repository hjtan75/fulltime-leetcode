class Solution:
    def numDecodings(self, s: str) -> int:
        # The brute force method would be to use a decision tree
        # The time complexity of that would be O(2^n) because at every position i
        # we have two decision
        
        # The better method would be to use divide and conquer with dynamic programming
        # To find the solution of n, we need to find the solution for n-1 or n-2
        # We cache the result,
        # The space complexity will be O(n), we need to O(n) time complexity to fill the cache

        dp = {len(s) : 1}

        def dfs(i):
            if i in dp:
                return dp[i]

            if s[i] == '0':
                return 0 

            res = dfs(i+1)
            if i < len(s) - 1:
                if s[i] == '1' or (s[i] == '2' and s[i+1] in '0123456'):
                    res += dfs(i+2)
            dp[i] = res
            return res

        return dfs(0)

