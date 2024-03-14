class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        # Assign two pointers, one at the start and one at the end
        # If the sum is short of the goal, advance the end ptr
        # if it is more than the goal, advance the start pointer
        # if the sum is the answer, res += 1
        # if the in front of the end pointer is 0, or end pointer is the final position
        # advance front pointer
        # if not advance end pointer
        # Back pointer is not inclusive
        count = {0: 1}
        curr_sum = 0
        total_subarrays = 0
        
        for num in nums:
            curr_sum += num
            if curr_sum - goal in count:
                total_subarrays += count[curr_sum - goal]
            count[curr_sum] = count.get(curr_sum, 0) + 1

        return total_subarrays

            