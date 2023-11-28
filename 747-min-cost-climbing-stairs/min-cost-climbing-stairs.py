class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        nums_steps = len(cost)

        cost1 = cost[:2]
        c1, c2 = cost[0], cost[1]

        # while len(cost1) < nums_steps:
        #     prev_min = min(cost1[-1], cost1[-2])
        #     cost1.append(cost[len(cost1)] + prev_min)

        for i in range(2, nums_steps):
            c1, c2 = c2, min(c1, c2) + cost[i]

        return min(c1, c2)
