class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        comb = []
        def dfs(val, s_idx):
            if val < 0:
                return
            
            if val == 0:
                res.append(comb.copy())
                return

            prev = -1
            for i in range(s_idx, len(candidates)):
                if prev == candidates[i]:
                    continue
                if val - candidates[i] < 0:
                    break
                comb.append(candidates[i])
                dfs(val - candidates[i], i+1)
                comb.pop()
                prev = candidates[i]


        dfs(target, 0)
        return res

'''
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(cur, pos, target):
            if target == 0:
                res.append(cur.copy())
                return
            if target <= 0:
                return

            prev = -1
            for i in range(pos, len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                backtrack(cur, i + 1, target - candidates[i])
                cur.pop()
                prev = candidates[i]

        backtrack([], 0, target)
        return res
'''
                