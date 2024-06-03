class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # The brute foce method would be to list every possible array
        # And the sum the element in the array to find out whether the sum is greater 
        # then the target
        # O(n^2) because we are listing out all the possible subarray

        # A rolling window, start and end are pointed at the start of the array
        # If we sum is smaller than the target, increament end
        # if sum is larger than the target, increasement start
        # if sum is equal, increament both indexes,
        # Edge cases: if not possible to sum up to target with in the array, return 0
        # TC: O(n)

        if sum(nums) < target:
            return 0

        start, end = 0, 0
        summ = 0
        min_length = len(nums) + 1 

        while start < len(nums) and end < len(nums):
            while end < len(nums) and summ < target:
                summ += nums[end]
                end += 1

            while start < end and summ >= target:
                min_length = min(min_length, end - start)
                summ -= nums[start]
                start += 1

        if min_length == len(nums) + 1:
            return 0
            
        return min_length

            