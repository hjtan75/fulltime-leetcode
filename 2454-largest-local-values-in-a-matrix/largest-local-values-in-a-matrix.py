class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        # For every new column added, we find the largest element in the row
        # add that to the set and remove the previous largest element in the set, 
        # find the largest element in the set
        # Instead of O(3n) to O(n)

        n, m = len(grid), len(grid[0])
        res = [[0 for _ in range(m-2)] for _ in range(n-2)]

        for i in range(n-2):
            prev = 0
            col_max_set = deque([])  
            for j_sq in range(3):
                col_max = 0
                for i_sq in range(3):
                    col_max = max(col_max, grid[i+i_sq][j_sq])
                col_max_set.append(col_max)

            res[i][0] = max(col_max_set)
            for j in range(3, m):
                col_max = 0
                for i_sq in range(3):
                    col_max = max(col_max, grid[i+i_sq][j])
                
                col_max_set.append(col_max)
                col_max_set.popleft()
                res[i][j-2] = max(col_max_set)

        return res


            
