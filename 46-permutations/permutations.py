class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        perm = []
        arr = nums.copy()

        def dfs(arr):
            if len(perm) == len(nums):
                res.append(perm.copy())
                return

            length = len(arr)
            for idx in range(length):
                perm.append(arr[idx])
                del arr[idx]
                dfs(arr)
                n = perm.pop()
                arr.insert(idx, n)

        dfs(arr)
        print(res)
        return res

            
                

            
