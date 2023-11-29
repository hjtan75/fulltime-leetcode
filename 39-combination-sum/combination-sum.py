class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        combination = []
        def dfs(val, s_idx):
            if val < 0:
                return
            
            if val == 0:
                print(combination)
                res.append(combination.copy())
                return

            for i in range(s_idx, len(candidates)):
                combination.append(candidates[i])
                dfs(val - candidates[i], i)
                combination.pop()
        dfs(target, 0)
        return res