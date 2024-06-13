class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # The brute force method is to test every character in the dictionary
        # THe time complexity wil be O(nmc), n is the number of character in s
        # m is the length of wordDict and c is the length of word in dict

        # This is a dynamic programming question
        # Got the save the previous state in dp
        # dp is false for all element i, and only true when element[i] could be represent 
        # as a segmentation of dictionary
        # so for very element in dictioary we check wheather it exist in s[i:i+w]
        # If it does mark i+w as true
        # Tc: O(nm) n == character in s and m is the length of dictionary

        dp = [False] * (len(s) + 1)

        i = 0
        dp[i] = True
        while i < len(s):
            if dp[i]:
                for word in wordDict:
                    if i + len(word) <= len(s) and not dp[i+len(word)] and s[i:i+len(word)] == word:
                        dp[i+len(word)] = True

            i += 1

        print(dp)
        return dp[-1]
