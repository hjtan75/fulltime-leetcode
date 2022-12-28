class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Memory complexity: O(n)
        # Time Complexity: O(26*n) because we gonna search the table every time
        # One little trick is that we don't have to find the max frequency of 
        # alphabet every time. It's only important when the a new max frequency 
        # show up
        numAlpha = [0] * 26
        firstIdx = 0
        secondIdx = 1
        # maxAlpha = ord(s[firstIdx]) - ord('A')
        maxFreq = 1
        longest = 0
        
        if len(s) <= 1:
            return 1
        
        numAlpha[ord(s[firstIdx]) - ord('A')] += 1
        numAlpha[ord(s[secondIdx]) - ord('A')] += 1
        if s[firstIdx] == s[secondIdx]:
            maxFreq += 1
        while True:
            if secondIdx - firstIdx + 1 - maxFreq <= k:
                longest = max(longest, secondIdx - firstIdx + 1)
                secondIdx += 1
                if secondIdx >= len(s):
                    break
                numAlpha[ord(s[secondIdx]) - ord('A')] += 1
                maxFreq = max(maxFreq, numAlpha[ord(s[secondIdx]) - ord('A')])
            else:
                numAlpha[ord(s[firstIdx]) - ord('A')] -= 1
                firstIdx += 1
                
            # maxExist = 0
            # for i in range(len(numAlpha)):
            #     if numAlpha[i] > maxExist:
            #         maxExist = numAlpha[i]
            #         maxAlpha = i
                    
            # print(longest, numAlpha)
                    
        return longest
        