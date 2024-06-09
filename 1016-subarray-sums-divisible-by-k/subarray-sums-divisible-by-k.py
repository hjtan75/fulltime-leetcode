class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Find all the posible subarray in nums and check if it's divisible by k
        # TC: O(n^3)
        # SP: O(1) for the sum variable

        # Use a prefix sum 
        # With prefix sum, we could have find the sum of an interval between i and j with O(n)
        # Reducing the listing possible array to O(n^2)
        # SP: O(n) for the prefix sum array 
        # Event O(n^2) will casue TLE

        # When current prefix % k = remainder
        # means that we have extrac value of remainder
        # In this case we have to subtract the remainder value
        # we need to have a previous prefix sum that has the remainder value
        # we use a hash map to hash {remainder value: count}
        # In location i, if we previously have the value of remainder
        # res += previously count of remainder
        # TC: O(n), we only parse through the array once
        # SP: O(n), we use a hashmap to mark the count of each prefix sum
        # Edge case, we add remainder to 0 with count 1 so means that the entire array
        # from 0 to current location has the sum that is divisible by k

        count = 0
        prefix_sum = 0
        prefix_map = {0: 1}  
        
        for num in nums:
            prefix_sum += num
            mod = prefix_sum % k
            if mod < 0:  
                mod += k
            if mod in prefix_map:
                count += prefix_map[mod]
                prefix_map[mod] += 1
            else:
                prefix_map[mod] = 1
        
        return count