class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        # This problem can be solve with a sliding window and hashtable
        # First expand the sliding window until the integer satisfy k
        # Keep expanding the window if the next element is in the hashtable
        # New element not in hashtable, shrink sliding window until k could be added in
        # Subarray with atmost k element = subarray of atmost k-1 elment + subarray of exactly k elment
        # Subarray of exactly k elment = subarray with atmost k element - subarray of atmost k-1 elment 
        # TC: O(n)
        def atmost_k_element(nums, k):
            res, l, r = 0, 0, 0
            count = {}
            n = len(nums)

            while r < n:
                count[nums[r]] = count.get(nums[r], 0) + 1
                while len(count) > k:
                    count[nums[l]] -= 1
                    if count[nums[l]] == 0:
                        del count[nums[l]]
                    l += 1
                res += r - l + 1
                r += 1
                print(res, r)
            return res

        atmost_k = atmost_k_element(nums, k)
        atmost_less_k = atmost_k_element(nums, k-1)
        return atmost_k - atmost_less_k

        
                    
                    