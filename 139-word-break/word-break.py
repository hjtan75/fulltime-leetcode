class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The brute force method would be trying every wordDict for each char in s
        # TC: O(m^n) n: number character in s and m: length of wordDict

        # This is a dynamic prograaming question, so i should store the previous result
        
        # I wanted to use a dicision tree mehod
        n = len(s)
        dp = [False] * (n+1)
        dp[0] = True

        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if i + len(w) <= n and s[i:i+len(w)] == w:
                        dp[i + len(w)] = dp[i]

        return dp[n]
