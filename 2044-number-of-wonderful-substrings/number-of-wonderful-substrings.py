class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        # We use bitmask for this task
        # Because the character is from a to j, we can represent it from 0000 0000 00 to 1000 0000 00
        # For each character, we add it into the prefix, we can do that with xor operation
        # For a substring bit mask is the same as the entire string, means that that is a even wonderful 
        # We need to consider scenario where at most odd, we flip a single bit on the bit mask then check
        # Whether it has been encountered before

        count = [0] * 1024 # Count the frequency of a bitmask
        res = 0
        bitmask = 0
        count[0] = 1 # We set the empty substring to be 1 because this mean the string itself is wonderfull

        for c in word:
            bitmask ^= (1<<ord(c) - ord('a'))
            # print("-", bitmask)
            res += count[bitmask]
            for i in range(10):
                res += count[bitmask ^ (1<<i)]
                # print(bitmask ^ (1<<i))
            count[bitmask] += 1

        return res