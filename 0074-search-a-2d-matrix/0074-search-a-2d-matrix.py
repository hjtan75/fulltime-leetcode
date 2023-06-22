class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ci, cj = 0, len(matrix) - 1
        
        while ci < len(matrix[0]) and cj >= 0:
            if matrix[cj][ci] == target:
                return True
            elif matrix[cj][ci] > target:
                cj -= 1
            else:
                ci += 1
        return False