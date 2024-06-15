class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # My intuition is something similar to bubble sort
        # Moving all zeroes to the back of the array though swapping with the next non-zero character
        # Starting from the back, starting to move swap zero in position i with non-zero positiion 
        # i+1
        # After finish swapping continue iterating in reverse on i
        # TC: O(n)
        # SP: O(1)
        # nums = [0,1,0,3,12]
        # nums = [0]

        first_zero_idx = len(nums) - 1
        while first_zero_idx >= 0:
            if nums[first_zero_idx] == 0:
                i = first_zero_idx
                while i < len(nums) - 1 and nums[i + 1] != 0:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]
                    i += 1

            first_zero_idx -= 1





        