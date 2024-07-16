class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # We could use the two pointer method
        # the first pointer pointed to the next position to be filled
        # the second pointer pointed to the non repeating number
        # Parse the entire array until the second pointer reaches the end
        # return the first pointer as k

        left, right = 0, 1

        while right < len(nums):
            while right < len(nums) and nums[right] == nums[left]:
                right += 1

            if right >= len(nums):
                break
            left += 1
            nums[left] = nums[right]
        
        return left+1