class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        # Because the xor operation is reversible but
        # performing xor on the same value
        # we can find each arr[i] = pref[i] ^ arr[0~(i-1)]
        # this require O(n) as it will perform a single operation
        # Across the array and O(n) space complexity
        # to store the result

        res = [pref[0]]

        for i in range(1, len(pref)):
            new_arr = pref[i] ^ pref[i-1]
            res.append(new_arr)

        return res

