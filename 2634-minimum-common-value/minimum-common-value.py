class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        # Use two pointers one for each array
        # If ptr1 is larger then ptr2, advance ptr2, vice versa
        # return the first encounter of common integer
        # return -1 if either array reached to end

        ptr1, ptr2 = 0, 0

        while ptr1 < len(nums1) and ptr2 < len(nums2):
            if nums1[ptr1] == nums2[ptr2]:
                return nums1[ptr1]
            elif nums1[ptr1] > nums2[ptr2]:
                ptr2 += 1
            else:
                ptr1 += 1

        return -1