class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.q = nums
        self.k = k
        heapq.heapify(self.q)
        while len(self.q) > self.k:
            heapq.heappop(self.q)
        
    def add(self, val: int) -> int:
        heapq.heappush(self.q, val)
        while len(self.q) > self.k:
            heapq.heappop(self.q)
        return heapq.nlargest(self.k, self.q)[-1]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)