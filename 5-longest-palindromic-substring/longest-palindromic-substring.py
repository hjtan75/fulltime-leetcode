class Solution:
    def longestPalindrome(self, s: str) -> str:
        # The brute force method would be parse through every i
        # Find if the string is a palindrom
        
        n = len(s)
        max_len = 0
        res = ''

        for i in range(n):
            l, r = i, i

            while l >= 0 and r < n and s[l] == s[r]:
                l -= 1
                r += 1

            if r-l-1 > max_len:
                max_len = r-l-1
                res = s[l+1:r]

            # Check for double mid palindrome
            if i < n - 1 and s[i] == s[i+1]:
                r = i + 1
                l = i

                while l >= 0 and r < n and s[l] == s[r]:
                    l -= 1
                    r += 1

                if r-l-1 > max_len:
                    max_len = r-l-1
                    res = s[l+1:r]


        return res
            