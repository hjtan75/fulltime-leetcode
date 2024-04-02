class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        transform_go = {}
        transform_back = {}
        n = len(s)

        for i in range(n):
            if s[i] in transform_go:
                if transform_go[s[i]] != t[i]:
                    return False
            elif t[i] in transform_back:
                if transform_back[t[i]] != s[i]:
                    return False
            else:
                transform_go[s[i]] = t[i]
                transform_back[t[i]] = s[i]


        return True 