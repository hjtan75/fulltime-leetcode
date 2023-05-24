class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Default dictionary automatically add new element when no key is found
        # We use mod to find which square does the small squares belongs to
        row_dict = collections.defaultdict(set)
        col_dict = collections.defaultdict(set)
        square_dict = collections.defaultdict(set)
        
        for r in range(0, 9):
            for c in range(0, 9):
                if board[r][c] == '.':
                    continue
                
                if board[r][c] in row_dict[r] or \
                board[r][c] in col_dict[c] or \
                board[r][c] in square_dict[(r // 3, c // 3)]:
                    return False
                
                row_dict[r].add(board[r][c])
                col_dict[c].add(board[r][c])
                square_dict[(r // 3, c // 3)].add(board[r][c])
                
                
        return True

                                