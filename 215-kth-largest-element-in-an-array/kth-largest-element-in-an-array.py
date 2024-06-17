import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # quick select is a method that could find kth largest element in avearge O(n)
        # the worst case for quick select would be O(n^2)
        # the easy way is to use sorting which require O(n log n)
        # SC: O(1)

        # we could use a heap to store the elmeents
        # heapifying the array would require O(n) time
        # Poping each element from heap would require O(log n)
        # it will require O(n + k log n)
        # SP: O(1)
        # arr = [1, 2, 3, 4, 5] 

        heapq.heapify(nums)

        for _ in range(len(nums) - k):
            heapq.heappop(nums)

        return heapq.heappop(nums)