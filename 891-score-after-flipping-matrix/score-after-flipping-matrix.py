class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # We can infinate moves,
        # The aim for row toggle, if to get as many 1 in the front as possible
        # The aim for col toggle, is to generate more 1 in the entire col
        # But which action do we carry out first? row or col?
        # We do row toggle first, because col will only increase the final value

        n, m = len(grid), len(grid[0])
        row_mask = 0

        for _ in range(m):
            row_mask <<= 1
            row_mask += 1

        for i in range(n):
            if grid[i][0] == 0:
                for j in range(m):
                    grid[i][j] = 1 - grid[i][j]

        # print(grid)
        for j in range(m):
            one_cnt = 0
            for i in range(n):
                if grid[i][j] == 1:
                    one_cnt += 1
                else:
                    one_cnt -= 1

            if one_cnt < 0:
                for i in range(n):
                    grid[i][j] = 1 - grid[i][j]

        # print(grid)
        res = 0
        for i in range(n):
            res += int(''.join(map(str, grid[i])), 2)

        return res