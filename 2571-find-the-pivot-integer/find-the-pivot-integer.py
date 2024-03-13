class Solution:
    def pivotInteger(self, n: int) -> int:
        # Assign two pointer 
        # Each will calculate the sum before it
        # Ptr that have the lesser sum will advance
        # If both ptr are the same, advance both ptr
        ptrl, ptrr, suml, sumr = 1, n, 0, 0

        while ptrl < ptrr:
            if suml == sumr:
                suml += ptrl
                sumr += ptrr
                ptrl += 1
                ptrr -= 1
            elif suml > sumr:
                sumr += ptrr
                ptrr -= 1
            else:
                suml += ptrl
                ptrl += 1

        if ptrl == ptrr and suml == sumr:
            return ptrr
        else:
            return -1