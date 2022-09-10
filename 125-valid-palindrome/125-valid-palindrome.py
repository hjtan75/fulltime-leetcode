class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        
        while(left < right):
            if not s[left].isalpha():
                if not s[left].isnumeric():
                    left += 1
                    continue
                left_c = s[left]
            else:
                left_c = s[left].lower()
            
            if not s[right].isalpha():
                if not s[right].isnumeric():
                    right -= 1
                    continue
                right_c = s[right]
            else:
                right_c = s[right].lower()
                
            
            if ord(left_c) != ord(right_c):
                return False
            
            left += 1
            right -= 1
            
            
        return True
            
        
        