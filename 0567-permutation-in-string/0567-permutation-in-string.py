class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # O(n*26) time complexity
        # n is the length of s2
        # 26 is to compare all the elements within the dictionary
        flagS1 = {}
        flagS2 = {}
        windowSize = len(s1)
        
        if len(s1) > len(s2):
            return False
        
        for c in 'abcdefghijklmnopqrstuvwxyz':
            flagS1[c] = 0
            flagS2[c] = 0
        
        for c in s1:
            flagS1[c] = flagS1.get(c) + 1
        
        for i in range(windowSize):
            flagS2[s2[i]] = flagS2.get(s2[i]) + 1
            
        if flagS1 == flagS2:
            return True 
            
        for i in range(len(s2) - windowSize):
            firstChar = s2[i]
            nextChar = s2[i+windowSize]
            
            flagS2[firstChar] = flagS2.get(firstChar) - 1;
            flagS2[nextChar] = flagS2.get(nextChar) + 1;
            
            if flagS1 == flagS2:
                return True
            
        
        return False