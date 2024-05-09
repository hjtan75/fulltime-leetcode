class Solution:
    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)
        res = 0
        
        for i in range(k):
            score = happiness[i] - i
            if score > 0:
                res += score
            else:
                break

        return res