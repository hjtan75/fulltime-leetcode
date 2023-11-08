class Solution:
    def reverse(self, x: int) -> int:
        s = str(x)
        s = s[::-1]
        neg = False
        
        if s[-1] == '-':
            nef = True
            s = s[:-1]
            ans = int(s)
            ans = -ans
        else:
            ans = int(s)

        
        if ans <= (2**31) - 1 and ans >= -(2**31):
            return ans
        else:
            return 0
            
        