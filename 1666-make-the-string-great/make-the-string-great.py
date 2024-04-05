class Solution:
    def makeGood(self, s: str) -> str:
        # TC: O(n!)
        delete_flag = True
        diff = abs(ord('A')-ord('a'))

        while delete_flag:
            delete_flag = False
            for i in range(len(s)-1):
                if abs(ord(s[i]) - ord(s[i+1])) == diff:
                    if i < len(s) - 2:
                        s = s[:i] + s[i+2:]
                    else:
                        s = s[:i]
                    delete_flag = True
                    break

        return s
                