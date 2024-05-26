class Solution:
    def checkRecord(self, s: str) -> bool:
        con_late = 0
        absent = 0

        for c in s:
            if c == 'A':
                absent += 1
            
            if c == 'L':
                con_late += 1
            else:
                con_late = 0

            if absent >= 2 or con_late >= 3:
                return False

        return True