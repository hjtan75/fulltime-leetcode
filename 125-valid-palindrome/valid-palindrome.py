class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue

            if not s[r].isalnum():
                r -= 1
                continue

            if s[l].isalpha():
                left_c = s[l].lower()
            else:
                left_c = s[l]

            if s[r].isalpha():
                right_c = s[r].lower()
            else:
                right_c = s[r]

            if left_c == right_c:
                l += 1
                r -= 1
            else:
                return False

        return True