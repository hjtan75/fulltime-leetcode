class Solution:
    def reorganizeString(self, s: str) -> str:
        # Use a array to record the occurance of alphabet
        # Convert into max heap the array from highest occurance to lowest
        # Alternative insert the highest and the second highest count character into string
        # Loop until ther are smaller than one item on the heap
        # If the last item has count = 1, add it too ans then return
        # If the last item has count > 1, return ""
        # Time: O(26log26){heapify} * O(n){every insertion}
        # Memory: O(n)

        cha_cnt = {}
        cnt_heap = []
        ans = []

        for c in s:
            cha_cnt[c] = cha_cnt.get(c, 0) + 1

        for cha, cnt in cha_cnt.items():
            cnt_heap.append([-cnt, cha])

        heapq.heapify(cnt_heap)
        while len(cnt_heap) >= 2:
            cnt1, cha1 = heapq.heappop(cnt_heap)
            cnt2, cha2 = heapq.heappop(cnt_heap)
            ans.append(cha1)
            ans.append(cha2)
            cnt1 += 1
            cnt2 += 1
            if cnt1 <= -1:
                heapq.heappush(cnt_heap, [cnt1, cha1])
            if cnt2 <= -1:
                heapq.heappush(cnt_heap, [cnt2, cha2])

        if len(cnt_heap) == 1:
            cnt, cha = heapq.heappop(cnt_heap)
            if cnt < -1:
                return ""
            else:
                ans.append(cha)


        return "".join(ans)