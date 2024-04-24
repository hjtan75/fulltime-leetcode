class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0

        if n == 1 or n == 2:
            return 1

        fb1, fb2, fb3, fb4 = 0, 1, 1, 2

        for i in range(3, n):
            fb1, fb2, fb3 = fb2, fb3, fb4
            fb4 = fb1+fb2+fb3

        return fb4