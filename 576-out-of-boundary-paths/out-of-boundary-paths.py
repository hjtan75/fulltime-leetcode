class Solution:
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        # Create a matrix that will keep updated by the number of way that could reach by the 
        # location of the ball
        # For each iteration, we carry out one move, so we update dp[i][j] with the number of
        # way to get to the location from the previous matrix
        # If dp[i][j] if the border, we add it to count
        # Time complexity: O(maxMove * n * m)

        M = 1000000007
        wayCntMatrix = [[0] * n for _ in range(m)]
        wayCntMatrix[startRow][startColumn] = 1
        res = 0

        for moves in range(maxMove):
            temp = [[0] * n for _ in range(m)]

            for i in range(m):
                for j in range(n):
                    if i == 0:
                        res = (res + wayCntMatrix[i][j]) % M
                    if i == m - 1:
                        res = (res + wayCntMatrix[i][j]) % M
                    if j == 0:
                        res = (res + wayCntMatrix[i][j]) % M
                    if j == n - 1:
                        res = (res + wayCntMatrix[i][j]) % M

                    temp[i][j] = (
                        ((wayCntMatrix[i-1][j] if i > 0 else 0) + (wayCntMatrix[i+1][j] if i < m-1 else 0)) % M +
                        ((wayCntMatrix[i][j-1] if j > 0 else 0) + (wayCntMatrix[i][j+1] if j < n-1 else 0)) % M
                    ) % M

            wayCntMatrix = temp

        return res
                    

