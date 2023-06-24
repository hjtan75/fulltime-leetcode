class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Find which row that main conatain the integer
        # From each row perform binary search
        
        top, bot = 0, len(matrix) - 1
        midRow = 0
        while top <= bot:
            midRow = int((bot + top) / 2)
            # print(top, bot)
            if matrix[midRow][-1] >= target and matrix[midRow][0] <= target:
                break
            elif matrix[midRow][0] > target:
                bot = midRow - 1
            else:
                top = midRow + 1
                
        if top > bot:
            return False
        # print(midRow)
        l, r  = 0, len(matrix[midRow]) - 1
        while l <= r:
            midCol = int((l + r) / 2)
            if matrix[midRow][midCol] == target:
                return True
            elif matrix[midRow][midCol] > target:
                r = midCol - 1
            else:
                l = midCol + 1
                
        return False

        
                
                
        
                