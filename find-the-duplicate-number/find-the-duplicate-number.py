class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        repeated = 0
        marker = [0] * len(nums)

        for num in nums:
            if marker[num] > 0:
                repeated = num
            else:
                marker[num] += 1
        return repeated