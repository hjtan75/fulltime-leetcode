class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Approach 1
        # Use counting method, if a farmland is encountered, heck it's upper and leftsidr
        # If those are not farmland, it's a new start of farmland, marked as new farmland
        # Add the starting position to hashmap and mark it as visited
        # if those are farmland, see what's the original starting position based on their visited value,
        # update the last postion in hashmap
        
        # Appraoch 2
        # apprach to dfs
        # One farmland is encountered, explore it using dfs
        # until the last corner is found

        n, m = len(land), len(land[0])
        visited = [[False for k in range(m)] for j in range(n)]
        res = []

        def explore(i, j):
            if visited[i][j] or land[i][j] == 0:
                return None
            
            r_1, c_1 =  i, j
            r_2, c_2 = dfs(i, j)
            return [r_1, c_1, r_2, c_2]
            

        def dfs(i, j):
            if visited[i][j] or land[i][j] == 0:
                return None
            
            visited[i][j] = True
            d1, d2 = None, None
            if i < n-1:
                d1 = dfs(i+1, j)
            if j < m-1:
                d2 = dfs(i, j+1)

            if not d1 and not d2:
                return [i, j]
            elif d1 == None:
                return d2
            else:
                return d1
            
        for i in range(n):
            for j in range(m):
                coord = explore(i, j)
                if coord != None:
                    res.append(coord)

        return res

