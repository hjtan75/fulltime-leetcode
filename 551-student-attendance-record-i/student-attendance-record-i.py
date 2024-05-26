class Solution:
    def checkRecord(self, s: str) -> bool:
        con_late = 0
        absent = 0
        prev_late = False

        for c in s:
            if c == 'A':
                absent += 1
                prev_late = False

            if c == 'P':
                prev_late = False
            
            if c == 'L':
                if prev_late:
                    con_late += 1
                else:
                    con_late = 1
                prev_late = True

            if absent >= 2 or con_late >= 3:
                return False

        return True