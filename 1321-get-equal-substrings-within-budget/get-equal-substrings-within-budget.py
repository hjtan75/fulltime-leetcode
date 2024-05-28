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
        l, r = 0, 0
        cost, max_length = 0, 0
        while r < n:
            cost += abs(ord(s[r]) - ord(t[r]))
            
            while cost > maxCost:
                cost -= abs(ord(s[l]) - ord(t[l]))
                l += 1

            max_length = max(max_length, r-l+1)
            r += 1
                    

        return max_length




