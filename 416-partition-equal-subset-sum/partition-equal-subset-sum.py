class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # The brute force method would be to find possible subset of the array
        # Then find that is that the half of the total sum
        # Finding every subset would require O(2^n) because for every position
        # at x, we need to consider whether to include that number

        # If we use memoization, if will cut the time down to only O(n)
        # We create an array with size n*2, the first dimension is that we didn't choose the 
        # element, the second element meant that we chose the element

        # Edge case where the sum can't divide by two
        if sum(nums) % 2 != 0:
            return False

        # Create a dp array with row as summ and i as index
        half = sum(nums) // 2
        current_row = [False for _ in range(half+1)]
        previous_row = [False for _ in range(half+1)]

        previous_row[0] = True
        for i in range(1, len(nums)+1):
            for j in range(half+1):
                if j - nums[i-1] >= 0:
                    current_row[j] = previous_row[j] | previous_row[j-nums[i-1]]
                else:
                    current_row[j] = previous_row[j]

            previous_row = current_row[:]

        return previous_row[half]
