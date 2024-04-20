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

        # Approach 3
        # Similar to approach 1, but instead comparing the current's cell left and upper cell
        # we try to expand the rectangular as big as possible
        # Than mark all element in the rectagle to as visited 
        # This we could eliminate of using a dictinary and 3D array to mark visited
        # We also save time on converting dictionary to array for return

        n, m = len(land), len(land[0])
        res = []
        visited = [[False for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1 and not visited[i][j]:
                    r_1, c_1 = i, j
                    r_2, c_2 = i, j
                    while r_2 < n - 1 and land[r_2+1][j] == 1:
                        r_2 += 1
                    while c_2 < m - 1 and land[i][c_2+1] == 1:
                        c_2 += 1

                    for r in range(r_1, r_2+1):
                        for c in range(c_1, c_2+1):
                            visited[r][c] = True
                    
                    res.append([r_1, c_1, r_2, c_2])

                visited[i][j] = True

        return res
    

