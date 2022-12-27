class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Use a sliding window to find the longest substring
        # both index with go through the sequence once
        # Each check of character exsited is O(n)
        # Time complexity will be O(n)
        
        firstIdx = 0
        secondIdx = 0
        longest = 0
        existed = set()
        
        if len(s) < 1:
            return 0
        
        if len(s) == 1:
            return 1
        
        existed.add(s[0])
        while secondIdx < len(s) - 1:
            secondIdx += 1
            newC = s[secondIdx]
        
            if newC in existed:
                while s[firstIdx] != newC:
                    existed.remove(s[firstIdx])
                    firstIdx += 1
                firstIdx += 1
            else:
                existed.add(newC)
                
            longest = max(secondIdx-firstIdx+1, longest)    
        
            # print(existed, firstIdx, secondIdx)
        return longest
            
                