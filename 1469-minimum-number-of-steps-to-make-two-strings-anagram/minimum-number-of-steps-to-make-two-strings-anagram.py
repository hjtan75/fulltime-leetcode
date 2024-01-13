class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # O(n) method
        # Parse first string and record the number of occurrance of alphabets
        # Parse the second string and subtrac from the number of occurrance
        # Add to occurance with abs() is equal to result

        res = 0
        occurance = [0] * 26

        for c in s:
            asci = ord(c) - ord('a')
            occurance[asci] += 1

        for c in t:
            asci = ord(c) - ord('a')
            occurance[asci] -= 1

        for occur in occurance:
            res += abs(occur)

        return int(res / 2)
        