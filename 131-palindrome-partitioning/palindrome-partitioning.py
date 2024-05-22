class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # O(n^n)
        res, par = [], []

        def dfs(idx):
            if idx == len(s):
                res.append(par.copy())
                return

            for j in range(idx, len(s)):
                if isPalin(idx, j):
                    par.append(s[idx:j+1])
                    dfs(j+1)
                    par.pop()

        def isPalin(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False

                l += 1
                r -= 1
        
            return True

        dfs(0)
        return res