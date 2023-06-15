class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        q = collections.deque() # store index
        l, r = 0, 0
        
        
        while r < len(nums):
            while q and nums[r] > nums[q[-1]]:
                q.pop()
            
            q.append(r)
            if l > q[0]:
                # Pop the element that is out of range
                q.popleft()
                
            if (r + 1) >= k:
                res.append(nums[q[0]])
                l += 1
                
            r += 1
            
        return res