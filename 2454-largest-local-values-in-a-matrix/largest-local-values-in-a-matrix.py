class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n, m = len(grid), len(grid[0])
        res = [[0 for _ in range(m-2)] for _ in range(n-2)]

        for i in range(n-2):
            for j in range(m-2):
                maxi = 0
                for i_sq in range(3):
                    for j_sq in range(3):
                        maxi = max(maxi, grid[i+i_sq][j+j_sq])

                res[i][j] = maxi

        return res

            
