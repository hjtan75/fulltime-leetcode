class Solution:
    def romanToInt(self, s: str) -> int:
        # Because we want to know whether the current character is a subtraction or a character itself
        # E.g. DIV = 504, but DVI is 506
        # The first case is a subtraction but the second case ia a addition
        # For every character, check whether the next character is larger than it
        # If it is, it's a subtraction, else it's a addtion

        maping = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s) - 1):
            if s[i] == 'I':
                if (s[i+1] == 'V' or s[i+1] == 'X'):
                    print('bug')
                    res -= 1
                else:
                    res += 1
            elif s[i] == 'V':
                res += 5
            elif s[i] == 'X':
                if (s[i+1] == 'L' or s[i+1] == 'C'):
                    res -= 10
                else:
                    res += 10
            elif s[i] == 'L':
                res += 50
            elif s[i] == 'C':
                if (s[i+1] == 'D' or s[i+1] == 'M'):
                    res -= 100
                else:
                    res += 100
            elif s[i] == 'D':
                res += 500
            else:
                res += 1000

        res += maping[s[-1]]

        return res
