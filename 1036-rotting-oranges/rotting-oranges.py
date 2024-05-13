class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # Use a array to record the new added rotten oranges,
        # For each while loop, check if new oranges is added and added one more minute
        # If yes loop, if no exit loop

        minute = 0
        rotten_oranges_1, rotten_oranges_2 = [], []
        n, m = len(grid), len(grid[0])
        rotten_visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    rotten_oranges_2.append([i, j])

        while len(rotten_oranges_2) != 0:
            minute += 1
            rotten_oranges_1, rotten_oranges_2 = rotten_oranges_2, rotten_oranges_1
            while rotten_oranges_1:
                i, j = rotten_oranges_1.pop()
                if i > 0 and grid[i-1][j] == 1:
                    rotten_oranges_2.append([i-1, j])
                    grid[i-1][j] = 2

                if j > 0 and grid[i][j-1] == 1:
                    rotten_oranges_2.append([i, j-1])
                    grid[i][j-1] = 2

                if i < n-1 and grid[i+1][j] == 1:
                    rotten_oranges_2.append([i+1, j])
                    grid[i+1][j] = 2

                if j < m-1 and grid[i][j+1] == 1:
                    rotten_oranges_2.append([i, j+1])
                    grid[i][j+1] = 2

            

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    return -1

        if minute > 0:
            return minute - 1
        else:
            return minute

                
