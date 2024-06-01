class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The brute force method would be trying every wordDict for each char in s
        # TC: O(m^n) n: number character in s and m: length of wordDict

        # This is a dynamic prograaming question, so i should store the previous result
        
        n = len(s)
        dp = [False] * (n+1)
        dp[n] = True # because empty string would match character

        for i in range(n-1, -1, -1):
            for w in wordDict:
                if len(w) + i <= n and s[i: i + len(w)] == w:
                    dp[i] = dp[i + len(w)]

                if dp[i]:
                    break
            
        print(dp)
        return dp[0] 
