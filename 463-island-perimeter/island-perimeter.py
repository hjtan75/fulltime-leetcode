class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # search for the first piece of land
        # expand the search recursivly, if the direction have no expansion, return 1 as the side
        # Marked the land -1 after it's visited
        row, col = len(grid), len(grid[0])
        visited = [[False]*col for _ in range(row)]

        def explore(i, j):
            print(i, j)
            if i < 0 or i >= row or j < 0 or j >= col or grid[i][j] == 0:
                return 1

            if grid[i][j] == -1:
                return 0

            grid[i][j] = -1
            return explore(i+1, j) + explore(i-1, j) + explore(i, j+1) + explore(i, j-1)

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    return explore(i, j)

        return 0 