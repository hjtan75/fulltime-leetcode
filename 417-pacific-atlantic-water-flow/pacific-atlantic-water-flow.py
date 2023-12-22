class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        num_row = len(heights)
        num_col = len(heights[0])
        pacific = set()
        atlantic = set()
        res = []

        def pacific_dfs(r, c):
            if (r, c) in pacific:
                return
            else:
                pacific.add((r, c))
                if r > 0 and (heights[r-1][c] >= heights[r][c]):
                    pacific_dfs(r-1, c)
                if r < num_row - 1 and (heights[r+1][c] >= heights[r][c]):
                    pacific_dfs(r+1, c)
                if c > 0 and (heights[r][c-1] >= heights[r][c]):
                    pacific_dfs(r, c-1)
                if c < num_col - 1 and (heights[r][c+1] >= heights[r][c]):
                    pacific_dfs(r, c+1)

        def altantic_dfs(r, c):
            if (r, c) in atlantic:
                return
            else:
                atlantic.add((r, c))
                if (r, c) in pacific:
                    res.append([r, c])
                if r > 0 and (heights[r-1][c] >= heights[r][c]):
                    altantic_dfs(r-1, c)
                if r < num_row - 1 and (heights[r+1][c] >= heights[r][c]):
                    altantic_dfs(r+1, c)
                if c > 0 and (heights[r][c-1] >= heights[r][c]):
                    altantic_dfs(r, c-1)
                if c < num_col - 1 and (heights[r][c+1] >= heights[r][c]):
                    altantic_dfs(r, c+1)

        for c in range(num_col):
            pacific_dfs(0, c)
            
        for r in range(num_row):
            pacific_dfs(r, 0)

        for c in range(num_col):
            altantic_dfs(num_row-1, c)
            
        for r in range(num_row):
            altantic_dfs(r, num_col-1)

        return res
                

