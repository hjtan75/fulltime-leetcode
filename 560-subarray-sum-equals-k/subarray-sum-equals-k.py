class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash table that makmaps prefix sum to the array index
        # current element i which is the sume of all previous element
        # we need find previous prefix so that , prefix[i] - prefix[j] = k
        # we will iterate through the array, and add the current value
        # to the overall summ, we check if k - overall sum in is our haash
        # is it exist, res += frequcy of the prefix sum
        # when we increament the overall summ in the hash map

        res = 0
        prefix_sum = 0
        counter = {0:1}

        for num in nums:
            prefix_sum += num
            if prefix_sum - k in counter:
                res += counter[prefix_sum - k]

            counter[prefix_sum] = counter.get(prefix_sum, 0) + 1

        return res
