class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_to_char = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv',  '9':'wxyz'}

        if len(digits) == 0:
            return []
        res, com = [], []
        def dfs(idx):
            if idx == len(digits):
                res.append(''.join(com))
                return

            for c in num_to_char[digits[idx]]:
                com.append(c)
                dfs(idx+1)
                com.pop()

        dfs(0)
        return res
