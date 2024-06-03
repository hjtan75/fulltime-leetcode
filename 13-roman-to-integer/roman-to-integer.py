class Solution:
    def romanToInt(self, s: str) -> int:
        # Because we want to know whether the current character is a subtraction or a character itself
        # E.g. DIV = 504, but DVI is 506
        # The first case is a subtraction but the second case ia a addition
        # For every character, check whether the next character is larger than it
        # If it is, it's a subtraction, else it's a addtion

        maping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            if i < len(s) - 1 and maping[s[i]] < maping[s[i+1]]:
                res -= maping[s[i]]
            else:
                res += maping[s[i]]

        return res
