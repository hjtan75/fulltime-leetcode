class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        s = set()
        ans = -1

        for num in nums:
            if -num in s:
                if abs(num) > ans:
                    ans = abs(num)
                s.remove(-num)
            s.add(num)

        return ans
