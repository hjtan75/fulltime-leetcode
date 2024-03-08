class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = {}
        max_freq, res = 0, 0

        for num in nums:
            freq[num] = freq.get(num, 0) + 1
            max_freq = max(max_freq, freq[num])

        for k, v in freq.items():
            if v == max_freq:
                res += v

        return res