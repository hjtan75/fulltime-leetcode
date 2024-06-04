class Solution:
    def longestPalindrome(self, s: str) -> int:
    # build a palindrome with the letter provided in s
    # count the occurance of every letter in s
    # Include every even number character
    # in the end add the largest odd number if there exist
    # else return the total sum of occurance of character that has the even number
    # O(n)
    # SP: O(1)

        cnt = {}
        for c in s:
            cnt[c] = cnt.get(c, 0) + 1

        total_even = 0
        odd = False
        for k, v in cnt.items():
            if v % 2 == 0:
                total_even += v
            else:
                total_even += v - 1
                odd = True

        if odd:
            return total_even + 1
        else:
            return total_even
