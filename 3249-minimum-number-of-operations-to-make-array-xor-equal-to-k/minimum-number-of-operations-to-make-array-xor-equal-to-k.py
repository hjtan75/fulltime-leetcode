class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # Use xor binary operator toward all the nums
        # then finally xor k
        # convert the answer to binary and calculate the number of 1 meaning 
        # The binary that we need to flip
        res = nums[0]
        n = len(nums)
        for i in range(1, n):
            res = res ^ nums[i]

        res = res ^ k
        count = 0
        while res:
            count += res & 1
            res >>= 1

        return count