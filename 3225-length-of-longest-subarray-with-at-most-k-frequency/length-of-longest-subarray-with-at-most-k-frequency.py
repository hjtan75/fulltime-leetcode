class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        # This problem could be solve with a sliding window
        # Use a hashmap to record the frequency within the window
        # if one of the frequncy goes beyond k, strink the window from the left until
        # all element is under k again
        # If all elements frequency is below K, expand window from the right
        n = len(nums)
        max_len, r, l = 0, 0, 0
        counter = {}

        while r < n and l <= r:
            counter[nums[r]] = counter.get(nums[r], 0) + 1
            while counter[nums[r]] > k:
                counter[nums[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r+=1

        return max_len