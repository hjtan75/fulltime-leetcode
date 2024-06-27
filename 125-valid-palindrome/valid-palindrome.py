class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = []

        for c in s:
            if c.isalnum():
                if c.isalpha():
                    cleaned_str.append(c.lower())
                else:
                    cleaned_str.append(c)

        if len(cleaned_str) == 0:
            return True

        l, r = 0, len(cleaned_str) - 1
        while l < r:
            if cleaned_str[l] == cleaned_str[r]:
                l += 1
                r -= 1
            else:
                return False

        return True