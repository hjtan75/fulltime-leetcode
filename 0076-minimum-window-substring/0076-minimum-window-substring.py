class Solution:
    def minWindow(self, s: str, t: str) -> str:
        winDict = {}
        winCount = 0
        needDict = {}
        needCount = 0
        shortest = []
        shortestLen = 100001
        
        for tc in t:
            if tc in needDict:
                needDict[tc] += 1
            else:
                needDict[tc] = 1
                needCount += 1
                winDict[tc] = 0
        
        lPtr = 0
        for rPtr in range(len(s)):
            c = s[rPtr]
            if c in winDict:
                winDict[c] += 1
                if winDict[c] == needDict[c]:
                    winCount += 1
                    
            while winCount == needCount:
                if (rPtr - lPtr + 1) < shortestLen:
                    shortest = [lPtr, rPtr]
                    shortestLen = rPtr - lPtr + 1
                
                if s[lPtr] in winDict:
                    winDict[s[lPtr]] -= 1
                    if winDict[s[lPtr]] < needDict[s[lPtr]]:
                        winCount -= 1
    
                lPtr += 1
        
                # print(lPtr, rPtr, winDict)
            
            
        # print(shortestLen, shortest)
        return s[shortest[0]:shortest[1]+1] if shortestLen != 100001 else ""
                