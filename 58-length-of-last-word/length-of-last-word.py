class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        char_count = 0

        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if char_count > 0:
                    break
                else:
                    continue
            else:
                char_count += 1

        return char_count