class Solution:
    def binarySearch(self, numbers, num):
        l = 0
        r = len(numbers) - 1
        
        while l <= r:
            # print(num, l, r)
            m = ceil((r + l) / 2)
            if numbers[m] == num:
                return m
            
            if num > numbers[m]:
                l = m + 1
            else:
                r = m - 1
        
        return -1 
    
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic = {}
        
        for i in range(int(len(numbers))):
            t = target - numbers[i]
            resultIdx = self.binarySearch(numbers[i+1:], t) + i + 1
            if resultIdx >= 0 and i != resultIdx:
                return [i+1, resultIdx+1]
            
            