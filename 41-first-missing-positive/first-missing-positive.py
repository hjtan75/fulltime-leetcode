class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # This places all element on the respective array column
        # We don't have to consider number > n because there will certain that a smaller
        # number exist before that.
        # TC: O(2n), one for putting every element to the respective place
        # The other used to parse the array for smallest integer
        # MC: O(1), because we only uses the original array
        # Swap function is compulsary because python funciton is pass by value, so the value could be sway
        # If not, python list is immutable, so the value don't change
        def swap(arr, i, j):
            arr[i], arr[j] = arr[j], arr[i]

        n = len(nums)

        for i in range(n):
            while 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
                swap(nums, i, nums[i] - 1)
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        return n + 1