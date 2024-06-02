class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is negative return false because negative number is not
        # a palindrom
        # Add the number into a array then calculate test whether it is palindrom
        if x < 0:
            return False 

        x_copy = x
        x_reverse = 0

        while x > 0:
            x_reverse = (x_reverse * 10) + (x % 10)
            x = x // 10

        return x_copy == x_reverse