class Solution:
    def specialArray(self, nums: List[int]) -> int:
        # Have to sort the array, which has TC O(n log n)
        # x is bound by the range [0, len(nums)]
        # for each x in range, calculate the number of element bigger than x
        # if not enough element bigger than x, reduce search range to [0, x-1]
        # if too many elements, reduce search range to [x+1, len(nums)]
        # if no element satisfy condition, return -1
        # Because nums is sorted, use binary search to find the elements that is bigger than x
        # TC = sorting + binary search O(n log n) + O(log^2 n) = O(log^2 n)
        # SC = O(1)

        l, r = 0, len(nums)
        nums = sorted(nums)
        if nums[0] > len(nums):
            return len(nums)

        while l <= r and (l+r) // 2 > 0 and (l+r) // 2 <= len(nums):
            m = (l + r) // 2
            
            l_num, r_num, m_num = 0, len(nums), 0
            while l_num <= r_num:
                m_num = (l_num + r_num) // 2
                if m_num <= 0 or m_num >= len(nums):
                    break
                if m <= nums[m_num]:
                    if m_num == 0 or (m_num > 0 and m > nums[m_num - 1]):
                        break
                    else:
                        r_num = m_num - 1
                else:
                    l_num = m_num + 1
            
            num_bigger = len(nums) - m_num
            if num_bigger == m:
                return m
            elif num_bigger > m:
                l = m + 1
            else:
                r = m - 1
        return -1 

