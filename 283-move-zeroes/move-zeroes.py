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
        # TC: O(n^2)
        # SP: O(1)
        # nums = [0,1,0,3,12]
        # nums = [0]

        # Optimize version
        # Because in every 0, we compare the same value as the previous zero
        # LIke in the list the second second in index 0 are being compare with 1, 3 and 12
        # while the second zero already being compared before with 3 and 12
        # How do we swap without alterting the order
        # what we can do is to use two pointer, both pointer start at index 0
        # One pointed to the next zero, the other pointed to a non-zero numbre
        # If pointer zero < pointer non-zero, swap those two, then continue to find the next value
        # This will have the time complexity of only TC:O(n) because we only iterate the array once
        # Edge cases the array only contain zero or only contain non zero, then
        # the either pointer will be out of range
        # [0,1,0,3,12]
        # [1,0,0,3,12]
        # [1,3,0,0,12]
        # [1,3,12,0,0]

        n_p, z_p = 0, 0
        while n_p < len(nums) and z_p < len(nums):
            while n_p < len(nums) and nums[n_p] == 0:
                n_p += 1

            while z_p < len(nums) and nums[z_p] != 0:
                z_p += 1

            if n_p < len(nums) and z_p < len(nums) and z_p < n_p:
                nums[z_p], nums[n_p] = nums[n_p], nums[z_p]
                z_p += 1
                n_p += 1
            else:
                n_p += 1








        