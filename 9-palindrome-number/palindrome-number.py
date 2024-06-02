class Solution:
    def isPalindrome(self, x: int) -> bool:
        # if x is negative return false because negative number is not
        # a palindrom
        # Add the number into a array then calculate test whether it is palindrom
        if x < 0:
            return False 

        arr = []
        while x > 0:
            arr.append(x % 10)
            x = x // 10

        i, j = 0, len(arr) - 1
        while i < j:
            if arr[i] == arr[j]:
                i += 1
                j -= 1
            else:
                return False

        return True