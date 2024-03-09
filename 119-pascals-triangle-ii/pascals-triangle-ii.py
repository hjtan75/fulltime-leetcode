class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Use two array exchangeabley to calculate the entire Pascal's triangle
        
        arr1, arr2 = [1], [1, 1]

        if rowIndex == 0:
            return arr1
        elif rowIndex == 1:
            return arr2

        for i in range(2, rowIndex + 1):
            arr1 = arr2.copy()
            arr2.clear()
            arr2.append(1)
            for j in range(0, len(arr1) - 1):
                arr2.append(arr1[j] + arr1[j+1])
            arr2.append(1)


        return arr2
