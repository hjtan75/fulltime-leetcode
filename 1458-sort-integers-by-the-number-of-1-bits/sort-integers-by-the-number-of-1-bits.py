class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        num_bit = []

        for v in arr:
            if v == 0:
                num_bit.append((0, 0))
            else:
                binary = bin(v)
                num_ones = 0
                for c in binary:
                    if c == '1':
                        num_ones += 1

                num_bit.append((num_ones, v))

        num_bit.sort()
        return map(lambda x: x[1],num_bit)
        