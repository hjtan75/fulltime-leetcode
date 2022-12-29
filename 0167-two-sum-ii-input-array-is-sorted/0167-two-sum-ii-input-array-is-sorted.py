class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # This method two sum method can only be used on a sorted array
        # Time complexity: O(n)
        # Memory complexity: O(1)
        l = 0
        r = len(numbers) - 1
        twoSum = numbers[l] + numbers[r]
        
        while twoSum != target:
            if twoSum > target:
                r -= 1
            else:
                l +=1
            twoSum = numbers[l] + numbers[r]
            
                
        return [l+1, r+1]
            
            