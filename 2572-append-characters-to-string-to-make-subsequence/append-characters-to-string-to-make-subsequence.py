class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        # two pointers pointer to the starting position of each string
        # Because i want t to be a subsequence of s, s  much contain all character in t
        # it must be in the same sequence.
        # For i and j be the pointer of s and t respectively, 
        # If the character is the same i++ and j++, if not i++
        # return len(t) - j, number of element needed to add to s so that all character in t
        # exist in s
        # TC: O(n) for n is the length of t

        s_idx, t_idx = 0, 0

        while s_idx < len(s) and t_idx < len(t):
            if s[s_idx] == t[t_idx]:
                t_idx += 1
            s_idx += 1

        return len(t) - t_idx


