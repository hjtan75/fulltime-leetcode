class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # The normal method which compare each element in nums
        # with it's neigbours, This will have a time
        # Complexity of O(n)

        # We need a solution that is O(log n)
        # First we check the the first and the last element
        # Whether that are larger than their neighbour
        # no two adjacent elements has the same value
        # The not first and last element, the peak will be larger than
        # first and last element 
        # Left start and end be the first and last element in the array
        # if the central point is in larger than start and last
        # strink the element by half depending on which neighbout is bigger
        # if the central is smallest than both start and end
        # it means there is a peak on both sides 
        # if central is in between start and end, there will be a peak on the 
        # larger side


        if len(nums) == 1:
            return 0

        if len(nums) < 2:
            if nums[0] > nums[1]:
                return 0
            else:
                return 1

        if nums[0] > nums[1]:
            return 0

        if nums[-1] > nums[-2]:
            return len(nums) - 1

        l, r = 0, len(nums) - 1

        while l <= r:
            m = int((l+r) / 2)

            if nums[m] > nums[m-1] and nums[m] > nums[m+1]:
                return m
                
            if nums[m] > nums[l] and nums[m] > nums[r]:
                if nums[m+1] > nums[m]:
                    l = m + 1
                else:
                    r = m - 1
            elif nums[m] <= nums[l] and nums[m] <= nums[r]:
                l = m + 1
            else:
                if nums[l] > nums[r]:
                    r = m - 1
                else:
                    l = m + 1


