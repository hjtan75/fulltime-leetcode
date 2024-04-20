class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        # Use counting method, if a farmland is encountered, heck it's upper and leftsidr
        # If those are not farmland, it's a new start of farmland, marked as new farmland
        # Add the starting position to hashmap and mark it as visited
        # if those are farmland, see what's the original starting position based on their visited value,
        # update the last postion in hashmap

        n, m = len(land), len(land[0])
        marking = {}
        visited = [[[0, 0] for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if land[i][j] == 1:
                    if i > 0 and land[i-1][j] == 1:
                        s_i, s_j = visited[i-1][j][0], visited[i-1][j][1]
                        visited[i][j][0] = s_i
                        visited[i][j][1] = s_j
                        marking["{} {}".format(s_i, s_j)] = "{} {}".format(i, j)
                    elif j > 0 and land[i][j-1] == 1:
                        s_i, s_j = visited[i][j-1][0], visited[i][j-1][1]
                        visited[i][j][0] = s_i
                        visited[i][j][1] = s_j
                        marking["{} {}".format(s_i, s_j)] = "{} {}".format(i, j)
                    else:
                        visited[i][j][0] = i
                        visited[i][j][1] = j
                        print(i, j)
                        marking["{} {}".format(i, j)] = "{} {}".format(i, j)
        res = []
        for k, v in marking.items():
            r_1, c_1 = map(int, k.split(" "))
            r_2, c_2 = map(int, v.split(" "))
            res.append([r_1, c_1, r_2, c_2])

        return res
