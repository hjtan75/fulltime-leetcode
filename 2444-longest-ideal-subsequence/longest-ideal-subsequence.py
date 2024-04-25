class Solution:
    def longestIdealString(self, s: str, k: int) -> int:
        # Use a 
        dp = [0] * 27
        n = len(s)

        for i in range(n-1, -1, -1):
            cha = s[i]
            idx = ord(cha) - ord('a')
            maxi = float(-100001)

            left = max((idx-k), 0)
            right = min((idx+k), 26)
            for j in range(left, right + 1):
                maxi = max(maxi, dp[j])

            dp[idx] = maxi + 1

        return max(dp)