class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # brute force method would be to store the frequency of each element in and array
        # then we sort it based on the frequency
        # we take the most requent k element

        # we can first sort the items then put them
        # we can count the iterm and the putthem in the min heap,
        # if heap size is more than k, pop heap O(1)
        # TC: O(n log n)
        # SP: O(k)

        counter = {}
        hheap = []
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for val, freq in counter.items():
            heapq.heappush(hheap, (freq, val))
            if len(hheap) > k:
                heapq.heappop(hheap)

        res = []
        for freq, val in list(hheap):
            res.append(val)

        return res