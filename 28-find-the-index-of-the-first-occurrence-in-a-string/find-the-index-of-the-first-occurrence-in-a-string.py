class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # This brute force method would be to check every position at haystack
        # Then compare it with needle
        # The TC: O(n*m) for n = len(haystack), m = len(needle)

        if len(needle) > len(haystack):
            return -1

        for hay_start in range(len(haystack)):
            hay_idx, nee_idx = hay_start, 0
            while hay_idx < len(haystack) and nee_idx < len(needle) and haystack[hay_idx] == needle[nee_idx]:
                hay_idx += 1
                nee_idx += 1

            if nee_idx == len(needle):
                return hay_idx - nee_idx


        return -1


            