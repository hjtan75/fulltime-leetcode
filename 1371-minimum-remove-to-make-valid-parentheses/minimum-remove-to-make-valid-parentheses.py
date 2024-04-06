class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Array to markdown location of '(',
        # When encounter a ')', pop from array,
        # If array is empty, remove ')'
        # Remove all leftover '(' after parsing the string
        # TC: O(n), will parse the string twice, one for checking paranthesis, the other for passing strings
        # MC: O(n), memory need to transfer string and array

        arr_l, arr_r, n = [], [], len(s)
        res = []

        for i in range(n):
            if s[i] == '(':
                arr_l.append(i)
            elif s[i] == ')':
                if len(arr_l) == 0:
                    arr_r.append(i)
                else:
                    arr_l.pop()

        print(arr_l)
        print(arr_r)
        for i in range(n):
            if i not in arr_l and i not in arr_r:
                res.append(s[i])

        return ''.join(res)