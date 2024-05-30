class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # The brute force method would be try every posibility
        # of i, j, k. This would have O(n^3) and to perform 
        # XOR calculations is would be O(n^4)

        # find a subarray with size > 2 that has the same value
        # Means that to find a subarray that has a xor 
        # value of 0. This reduce the TC O(n^3)
        # Because we know that the reverse operation of a xor is just xor with the same value
        # we and create a prefix xor array which we can find the xor for any i and j with O(1) TC
        # We need to find all posibiity of i and j that will result in xor 
        # for every i and j that has a result of 0, ad len - 1 to the result
        # The first element of a prefix sum is a dummy for easier calculation
        # TC: O(n^2) every possibility of prefix 
        # SC: O(n) prefix array

        prefix = [0]
        res, n = 0 , len(arr)
        for i in range(n):
            prefix.append(arr[i] ^ prefix[i])

        for i in range(n+1):
            for j in range(i+1, n+1):
                if prefix[i] ^ prefix[j] == 0:
                    print(i, j)
                    res += j - i - 1

        return res