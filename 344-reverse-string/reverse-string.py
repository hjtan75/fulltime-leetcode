class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Not extra memory, so we have two pointers
        # One pointed to the first element and one to the last
        # We swap the value between those to cells and the increament the start
        # pointer and decreasement the last pointer until start <= end

        start, end = 0, len(s) - 1

        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

        return s

        