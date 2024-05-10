class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        # I think this will be a two pointer question
        # The fact that the array in sorted make it that we don't have to solve it in try
        # Every possibility

        ans = []
        n = len(arr)

        for i in range(n):
            for j in range(i+1, n):
                ans.append((arr[i]/arr[j], [arr[i], arr[j]]))

        ans.sort()
        # print(list(ans[k])[1])
        return list(ans[k-1])[1]