class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # The brute force method would be parsing every single possible subarray
        # then perform multiplcation O(n)
        # TC: O(n^3)
        
        # Another method would be to use prefix product
        # Create any array with a a prefix product
        # Find the every possible i and j then use it to find the multiplication with only O(1)
        # TC: O(n^2)

        # we use dynamic programming method. 
        # At each subarray, the result will depend on the previous subarray
        # Because of negative number will convert smallest number to the largest
        # we need to remember max and min for each subarray
        # the min will come in handy when negative number is encountered
        # The edge case is zero, when we encounter a zero, reset min, max to 0
        
        mini, maxi = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                mini, maxi = 1, 1
                continue

            tmp = maxi * n
            maxi = max(maxi*n, mini*n, n)
            mini = min(tmp, mini*n, n)
            res = max(res, maxi)

        return res
            

        
