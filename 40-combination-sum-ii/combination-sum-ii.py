class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        def dfs(val, s_idx):
            if val < 0:
                return
            
            if val == 0:
                str_com = map(str, sorted(combination))
                str_com = " ".join(str_com)
                res.add(str_com)
                return

            prev = -1
            for i in range(s_idx+1, len(candidates)):
                if prev == candidates[i]:
                    continue
                combination.append(candidates[i])
                dfs(val - candidates[i], i)
                combination.pop()
                prev = candidates[i]

    
        for i in range(len(candidates)):
            combination = [candidates[i]]
            dfs(target - candidates[i], i)

        list_ans = []
        while res:
            str_com = res.pop()
            str_com = str_com.split(" ")
            list_ans.append(map(int, str_com))
        return list_ans
                