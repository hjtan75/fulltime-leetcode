class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        ranker = []
        n = len(score)

        for i in range(n):
            ranker.append((score[i], i))

        ranker.sort(reverse=True)

        res = [""] * n
        for i in range(n):
            sco, idx = ranker[i]
            if i == 0:
                res[idx] = 'Gold Medal'
            elif i == 1:
                res[idx] = 'Silver Medal'
            elif i == 2:
                res[idx] = 'Bronze Medal'
            else:
                res[idx] = str(i+1)

        return res
            

            