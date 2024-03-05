class Solution:
    def minimumLength(self, s: str) -> int:
        # Create two pointer, one from the left and the other from the right
        # Test if the character of the two pointer is the same, if not return the string
        # Advanced thw two pointer if the next character is the same, need to check that two pointer doesn't collide
        # return the string trim by the two pointer

        l, r = 0, len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l_prev, r_prev = s[l], s[r]
                while s[l] == l_prev and l < r:
                    l_prev = s[l]
                    l += 1

                if l >= r:
                    return 0

                while s[r] == r_prev and l < r:
                    r_prev = s[r]
                    r -= 1
                
            else:
                return r - l + 1

        return 1