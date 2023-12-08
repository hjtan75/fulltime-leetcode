class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ini_cell = []
        row = len(board)
        col = len(board[0])

        for i in range(row):
            for j in range(col):
                if board[i][j] == word[0]:
                    ini_cell.append([i, j])

        def backtracking(word_idx, i, j, visited):
            loc_str = f'{i} {j}'
            if word[word_idx] == board[i][j] and loc_str not in visited:
                if word_idx == len(word) - 1:
                    return True

                visited.add(loc_str)
                r1, r2, r3, r4 = None, None, None, None
                if i > 0:
                    r1 = backtracking(word_idx+1, i-1, j, visited)
                if i < row - 1:
                    r2 = backtracking(word_idx+1, i+1, j, visited)
                if j > 0:
                    r3 = backtracking(word_idx+1, i, j-1, visited)
                if j < col - 1:
                    r4 = backtracking(word_idx+1, i, j+1, visited)
                visited.remove(loc_str)

                return r1 or r2 or r3 or r4
            else:
                # if word[word_idx] != board[i][j]:
                    # print(visited)
                    # print('----', i, j, word[word_idx], board[i][j])
                return False

        for i, j in ini_cell:
            # print(i, j)
            if backtracking(0, i, j, set()):
                return True

        return False



        