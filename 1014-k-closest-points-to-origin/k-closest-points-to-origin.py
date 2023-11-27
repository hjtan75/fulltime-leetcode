class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        res = []

        for x, y in points:
            distance.append((x**2 + y**2, [x, y]))

        heapq.heapify(distance)
        for d in heapq.nsmallest(k, distance):
            res.append(d[1])
        return res
        