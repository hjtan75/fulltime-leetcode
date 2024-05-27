class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Have to sort the array, which has TC O(n log n)
        # x is bound by the range [0, len(nums)]
        # for each x in range, calculate the number of element bigger than x
        # if not enough element bigger than x, reduce search range to [0, x-1]
        # if too many elements, reduce search range to [x+1, len(nums)]
        # if no element satisfy condition, return -1
        # Because nums is sorted, use binary search to find the elements that is bigger than x
        # TC = sorting + binary search O(n log n) + O(2 log n) = O(n log n)
        # SC = O(1)

        l, r = 0, len(nums)
        nums = sorted(nums)

        while l <= r and (l+r) // 2 >= 0 and (l+r) // 2 < len(nums):
            m = (l + r) // 2
            idx = len(nums) - 1
            while idx >= 0 and nums[idx] >= m:
                idx -= 1

            num_bigger_m = len(nums) - idx - 1
            if m == num_bigger_m:
                return m
            elif m < num_bigger_m:
                l = m + 1
            else:
                r = m - 1

        
        if (l+r) // 2 == len(nums) and nums[0] >= len(nums):
            return len(nums)
        return -1 

