class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        firstDict = {}
        secondDict = {}
        
        for c in s:
            if c in firstDict:
                firstDict[c] += 1
            else:
                firstDict[c] = 1
                
        for c in t:
            if c in secondDict:
                secondDict[c] += 1
            else:
                secondDict[c] = 1
                
        if firstDict == secondDict:
            return True
        else:
            return False