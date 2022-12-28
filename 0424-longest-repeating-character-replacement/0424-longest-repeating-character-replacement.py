class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Memory complexity: O(n)
        # Time Complexity: O(n^2)
        numAlpha = [0] * 26
        firstIdx = 0
        secondIdx = 1
        maxAlpha = ord(s[firstIdx]) - ord('A')
        longest = 0
        
        if len(s) <= 1:
            return 1
        
        numAlpha[maxAlpha] += 1
        numAlpha[ord(s[secondIdx]) - ord('A')] += 1
        while True:
            if secondIdx - firstIdx + 1 - numAlpha[maxAlpha] <= k:
                longest = max(longest, secondIdx - firstIdx + 1)
                secondIdx += 1
                if secondIdx >= len(s):
                    break
                numAlpha[ord(s[secondIdx]) - ord('A')] += 1
            else:
                numAlpha[ord(s[firstIdx]) - ord('A')] -= 1
                firstIdx += 1
                
            maxExist = 0
            for i in range(len(numAlpha)):
                if numAlpha[i] > maxExist:
                    maxExist = numAlpha[i]
                    maxAlpha = i
                    
            # print(longest, numAlpha)
                    
        return longest
        