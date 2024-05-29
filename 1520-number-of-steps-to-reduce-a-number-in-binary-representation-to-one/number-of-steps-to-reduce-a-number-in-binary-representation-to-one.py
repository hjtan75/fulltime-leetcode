class Solution:
    def numSteps(self, s: str) -> int:
        # The straight forward method is to convert it into integer
        # Then process it to reduce in that way
        
        # The other method would be process it directly in binary
        # If number if even, lsb would be 0, just have to pop it
        # if it is 1, add 1 to the next available zero, the frequency of 1 coontingous to the number of 
        # step. beause it would be zero and we can divide it anyway

        carry, step = False, 0
        l = len(s) -1 
        while l > 0:
            if int(s[l]) + carry == 0:
                carry = 0
                step += 1
            elif int(s[l]) + carry == 2:
                carry = 1
                step += 1
            else:
                carry = 1
                step += 2
            l -= 1

        if carry == 1:
            step += 1

        return step
        