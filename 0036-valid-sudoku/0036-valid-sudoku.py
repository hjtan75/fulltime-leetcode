class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Square check
        for corner_j in range(0, 9, 3):
            for corner_i in range(0, 9, 3):
                check_list = [0]*9
                for j in range(corner_j, corner_j+3, 1):
                    for i in range(corner_i, corner_i+3, 1):
                        if board[j][i] != '.':
                            num = int(board[j][i]) - 1
                            if check_list[num] == 1:
                                return False
                            else:
                                check_list[num] = 1
                            
        # Row check
        for j in range(0, 9):
            check_list = [0]*9
            for i in range(0, 9):
                if board[j][i] != '.':
                    num = int(board[j][i]) - 1
                    if check_list[num] == 1:
                        return False
                    else:
                        check_list[num] = 1
                        
        # Column check
        for j in range(0, 9):
            check_list = [0]*9
            for i in range(0, 9):
                if board[i][j] != '.':
                    num = int(board[i][j]) - 1
                    if check_list[num] == 1:
                        return False
                    else:
                        check_list[num] = 1
                        
        return True

                                