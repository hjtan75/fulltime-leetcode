class Solution:
    def rob(self, nums: List[int]) -> int:
        # Use dp to solve this question
        # Create a array, this array state the maximum money could be drawn from the location nums[i]
        # dp1 uses first element, but not the last
        # dp2 uses second element, but also the last
        # TC: O(n)
        # MC: O(n)

        n = len(nums)

        if n <= 3:
            return max(nums)

        dp1 = [0] * (n-1)
        dp2 = [0] * (n-1)
        dp1[0], dp1[1], dp1[2] = nums[0], nums[1], nums[2] + nums[0]
        dp2[0], dp2[1], dp2[2] = nums[1], nums[2], nums[3] + nums[1]

        for i in range(3, n-1):
            dp1[i] = max(dp1[i-2], dp1[i-3]) + nums[i]

        for i in range(4, n):
            dp2[i-1] = max(dp2[i-3], dp2[i-4]) + nums[i]
        
        print(dp1)
        print(dp2)
        return max(max(dp1[-1], dp1[-2]), max(dp2[-1], dp2[-2]))


        