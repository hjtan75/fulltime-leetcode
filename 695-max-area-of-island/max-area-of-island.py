class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Utilize union find
        # O(n + )
        n_row = len(grid)
        n_col = len(grid[0])
        parent = [-1 for i in range(n_row * n_col)]
        size = [0 for i in range(n_row * n_col)]

        def find(a):
            # O(n)
            while parent[a] != a:
                a = parent[a]
            return a

        def union(a, b):
            # O(1)
            parent_a = find(a)
            parent_b = find(b)

            if parent_a != parent_b:
                if size[parent_a] < size[parent_b]:
                    parent[parent_b] = parent_a
                    size[parent_a] = size[parent_b] + size[parent_a] 
                else:
                    parent[parent_a] = parent_b
                    size[parent_b] = size[parent_b] + size[parent_a] 
            
        def cell_parsing():
            for i in range(n_row):
                for j in range(n_col):
                    if grid[i][j] == 1:
                        idx = i*n_col + j
                        parent[idx] = idx
                        size[idx] = 1
                        if i != 0 and grid[i-1][j] == 1:
                                union(idx, idx - n_col)

                        if j != 0 and grid[i][j-1] == 1:
                                union(idx, idx - 1)

            max_size = 0
            for i in range(len(parent)):
                if i == parent[i] and size[i] > max_size:
                    max_size = size[i]

            return max_size

        return cell_parsing()