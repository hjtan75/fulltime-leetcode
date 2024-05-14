class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        # The brute force method is to try to start at every position
        # That will be O(n^3)
        # Use a recursive method to all all direction
        # Choose the highest amount an return the value + the value of current cell

        n, m, = len(grid), len(grid[0])
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        res = 0

        def explore(i, j, visited):
            if i < 0 or i >= n or j < 0 or j >= m or visited[i][j] or grid[i][j] == 0:
                return 0

            visited[i][j] = True
            max_return = 0
            for r, c in direction:
                max_return = max(max_return, explore(i+r, j+c, visited))

            visited[i][j] = False
            return max_return + grid[i][j]

        for i in range(n):
            for j in range(m):
                visited = [[False for _ in range(m)] for _ in range(n)]
                score = explore(i, j, visited)
                res = max(res, score)
                # print(i, j, score)

        return res
