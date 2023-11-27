class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -(heapq.heappop(stones))
            x = -(heapq.heappop(stones))
            if y - x > 0:
                heapq.heappush(stones, x-y)

        if len(stones) == 0:
            return 0
        else:
            return -stones[0]