class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        # the brute force method would to start at every position at s
        # then transfrom to t based on the maxcost
        # Mark the longest substring create
        # TC: O(n^2) SC: O(1) a pointer marking the index

        # Calculate the cost to change for each character
        # Need to find the maximum length with maxCost as contraint
        # The can be achieve with a roling window
        # When we are over max cost increase left boundary, when
        # we have maxCost left, increase right bounary, mark the longest length
        # TC: O(n) both pointer only pass through array once
        # SC: O(n) Array to store the difference

        n = len(s)
        diff = [0] * n

        for i in range(n):
            diff[i] = abs(ord(s[i]) - ord(t[i]))
        # print(diff)
        l, r = 0, 0
        cost, max_length = 0, 0
        while r < n:
            cost += diff[r]
            if cost <= maxCost:
                # print(l, r, cost)
                max_length = max(max_length, r-l+1)
                r += 1
            else:
                cost -= diff[l]
                cost -= diff[r]
                l += 1
                if l > r:
                    cost += diff[r]
                    r = l
                    

        return max_length

            


        return max_length



