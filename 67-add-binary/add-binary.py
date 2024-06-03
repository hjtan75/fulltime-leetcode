class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # parse both a and b from the lsb to msb
        # perfrom addtion with include of carry
        # stop while loop when a either string reaches beyond the starting position
        # Add the remaining string and carry into answer

        res = []
        carry = 0
        i = 1

        if len(b) > len(a):
            a, b = b, a

        while i <= len(b):
            s = int(a[-i]) + int(b[-i]) + carry
            carry = s // 2
            res.append(str(s % 2))
            i += 1

        while i <= len(a):
            s = int(a[-i]) + carry
            carry = s // 2
            res.append(str(s%2))
            i += 1

        if carry > 0:
            res.append(str(carry))

        return "".join(res[::-1])