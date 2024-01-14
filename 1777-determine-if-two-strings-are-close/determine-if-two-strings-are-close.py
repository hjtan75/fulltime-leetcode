class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # Time: O(n log n)
        # Memory: O(n)
        # Operation is just swapping character, so need to record number of occurrance
        # Record the number of occurance for two strings
        # Sort two array by the number of occurance
        # if both array are the same then return true else false
        # ** Because we cannot swap between zero-occurrance with occurred, 
        # ** we first have to check if we trying to swap between zero-occurance and non-zero occurrance

        if len(word1) != len(word2):
            return False
        occur1 = [0] * 26
        occur2 = [0] * 26

        for c in word1:
            asci = ord(c) - ord('a')
            occur1[asci] += 1

        for c in word2:
            asci = ord(c) - ord('a')
            occur2[asci] += 1

        for i in range(len(occur1)):
            # if (occur1[i] == 0 and occur2[i] != 0) or (occur1[i] != 0 and occur2[i] == 0):
            if (occur1[i] == 0) ^ (occur2[i] == 0):
                return False

        occur1.sort()
        occur2.sort()

        for i in range(len(occur1)):
            if occur1[i] != occur2[i]:
                return False

        return True

        