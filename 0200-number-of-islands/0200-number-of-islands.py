
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows, cols = len(grid), len(grid[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        numIsland = 0
        
        def bfs(r, c):
            q = collections.deque()
            visited[r][c] = 1
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if r in range(rows) and c in range(cols) and grid[r][c] == "1" and \
                    visited[r][c] == 0:
                        q.append((r, c))
                        visited[r][c] = 1



        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1" and visited[row][col] == 0:
                    numIsland += 1
                    bfs(row, col)
                    
        return numIsland


        