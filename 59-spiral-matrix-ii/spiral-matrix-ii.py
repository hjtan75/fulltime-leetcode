class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        matrix = [[0]*n for _ in range(n)]
        corner = 0
        length = n
        currentNum = 1
        maxNum = n**2

        while currentNum <= maxNum:
            # Right 
            for step in range(0, length):
                matrix[corner][corner+step] = currentNum
                print(corner, corner+step, currentNum)
                currentNum += 1
            if currentNum >= maxNum:
                break
            # Down
            for step in range(0, length - 1):
                matrix[corner+1+step][corner+length-1] = currentNum
                print(corner+1+step, corner+length-1, currentNum)
                currentNum += 1
            # Left
            for step in range(0, length - 1):
                matrix[corner+length-1][corner+length-2-step] = currentNum
                print(corner+length-1, corner+length-2-step, currentNum)
                currentNum += 1
            # Up
            for step in range(0, length - 2):
                matrix[corner+length-2-step][corner] = currentNum
                print(corner+length-2-step, corner, currentNum)
                currentNum += 1

            
            corner += 1
            length -= 2
        return matrix