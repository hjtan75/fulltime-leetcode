class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # h >= pile.length
        # Use binary search to search through all the available k
        def testSpeed(piles, k):
            if k <= 0:
                return False
            
            time = 0
            for banana in piles:
                time += math.ceil(banana/k)
                # print(k, 'Time added', math.ceil(banana/k))
                if time > h:
                    return False
                
            return True

        l, r = 1, max(piles)
        while l <= r:
            speed = int((l+r)/2)
            currentSpeedTest = testSpeed(piles, speed)
            minusOneSpeedTest = testSpeed(piles, speed - 1)
            if currentSpeedTest and not minusOneSpeedTest:
                return speed
            
            if currentSpeedTest:
                r = speed - 1
            else:
                l = speed + 1
                
        return -1
            
                    