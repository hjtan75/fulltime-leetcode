class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Parse through every block with two for loop
        # If encounter a land, use dfs method to explore every direction
        # mark every land as visited when explored

        
        res = 0
        n, m = len(grid), len(grid[0])
        visited = [[False]*m for _ in range(n)]

        def explore(i, j):
            if visited[i][j] or grid[i][j] == "0":
                return 0

            visited[i][j] = True
            if i < n-1:
                explore(i+1, j)
            if i > 0:
                explore(i-1, j)
            if j < m-1:
                explore(i, j+1)
            if j > 0:
                explore(i, j-1)
            return 1

        for i in range(n):
            for j in range(m):
                res += explore(i, j)

        return res
