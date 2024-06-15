class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        # Iterate through row,
        # For every row iteration, we jump to next step by i-1 and j + 1
        # check whether it's within the rage bgore printing
        # O(nm) n is number of row, m is the number of column
        # SP: O(1)

        # we can leave and index for every row, we print if the index is within length
        # This is better for even array
        # But this will require O(n) space complexity
        # we create an array that store the position of the current row
        # if not  

        arr = []

        for i in range(len(nums)):
            for j in range(len(nums[i])):
                arr.append((i+j, j, nums[i][j]))

        arr.sort()
        res = []
        for summ, row, val in arr:
            res.append(val)


        return res