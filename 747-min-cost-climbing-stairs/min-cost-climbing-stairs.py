class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nums_steps = len(cost)

        cost1 = cost[:2]

        while len(cost1) < nums_steps:
            prev_min = min(cost1[-1], cost1[-2])
            cost1.append(cost[len(cost1)] + prev_min)

        # print(cost1)
        return min(cost1[-1], cost1[-2])
