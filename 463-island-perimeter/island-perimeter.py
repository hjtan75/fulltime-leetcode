class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # Appoarch 1: DFS
        # search for the first piece of land
        # expand the search recursivly, if the direction have no expansion, return 1 as the side
        # Marked the land -1 after it's visited
        # TC: O(n), MC: O(n)

        # Appoarch 2: Counting
        # if land == 1, perimeter += 1
        # If the upper or left land of the current area is land
        # We must subtract perimeter -2 because one side of neighbor and one side of current does not count
        row, col = len(grid), len(grid[0])
        perimeter = 0

        for i in range(row):
            for j in range(col):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i-1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:
                        perimeter -= 2

        return perimeter