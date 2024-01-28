class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # Create matrix with size row = len(text1) and col = len(text2)

        num_row = len(text1)
        num_col = len(text2)

        dp = [[0] * num_col for _ in range(num_row)]

        # Populate first column
        for i in range(num_row):
            if i == 0:
                dp[i][0] = 1 if text1[i] == text2[0] else 0
            else:
                if text1[i] == text2[0]:
                    dp[i][0] = 1
                else:
                    dp[i][0] = dp[i-1][0]

        # Populate first row
        for j in range(num_col):
            if j == 0:
                dp[0][j] = 1 if text1[0] == text2[j] else 0
            else:
                if text1[0] == text2[j]:
                    dp[0][j] = 1
                else:
                    dp[0][j] = dp[0][j-1]

        # Populate the rest of the matrix
        for i in range(1, num_row):
            for j in range(1, num_col):
                if text1[i] == text2[j]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])

        return dp[num_row-1][num_col-1]