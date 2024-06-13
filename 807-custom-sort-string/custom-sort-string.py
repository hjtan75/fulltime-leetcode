class Solution:
    def customSortString(self, order: str, s: str) -> str:
        # Because all character in order is unique
        # we can count the character is s and rearrange them in a way that it follows the 
        # order, because s might be bigger than order, so if order is if and s is ifif
        # should be rearragne to iiff, 
        # after appending all the character in order, we append the rest of the character of s
        # Tc: O(n) because we parse though s one, anad because order is limit by 26, so it's O(1)
        # SP: O(1) because character is bound by 26

        counter = {}
        res = []

        for c in s:
            counter[c] = counter.get(c, 0) + 1

        for c in order:
            if c in counter:
                res.append(''.join([c for _ in range(counter[c])]))
                counter[c] = 0

        for cha, occ in counter.items():
            if occ > 0:
                res.append(''.join([cha for _ in range(occ)]))

        return ''.join(res)