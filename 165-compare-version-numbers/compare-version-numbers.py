class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # For each revision compare it's value by 
        # Converting the string into int, return if one is larger than another
        # If the same move on to the next revision

        idx_1, idx_2 = 0, 0
        n_1, n_2 = len(version1), len(version2)

        while idx_1 < n_1 or idx_2 < n_2:
            len_1, len_2 = 0, 0
            while idx_1 + len_1 < n_1 and version1[idx_1 + len_1] != '.':
                len_1 += 1

            while idx_2 + len_2 < n_2 and version2[idx_2 + len_2] != '.':
                len_2 += 1

            devision_1 = int('0' + version1[idx_1:idx_1+len_1])
            devision_2 = int('0' + version2[idx_2:idx_2+len_2])
            if devision_1 < devision_2:
                return -1
            elif devision_2 < devision_1:
                return 1
            else:
                idx_1 += len_1 + 1
                idx_2 += len_2 + 1

        return 0 