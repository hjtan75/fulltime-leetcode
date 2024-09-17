class Solution {
public:
    int findTheLongestSubstring(string s) {
        // Will rolling window work on this questions?
        // when should we decide to decrease and increase the size of the window
        // The brute force method would cost O(n^3)
        // Try every possiblity and remember the appearance O(n^2)

        // Use a bitmask to calculate the counts of the vowels
        // Calculate the prefix count at every location
        // Parse through every location to find the longest substring
        int len = s.size();
        int bitmask = 0;
        int maxLen = 0;
        vector<int> seenMask(32, -2);
        seenMask[0] = -1;

        for(int i = 0; i < len; i++) {
            switch(s[i]) {
                case 'a':
                    bitmask = bitmask ^ (1 << 4);
                    break;
                case 'e':
                    bitmask = bitmask ^ (1 << 3);
                    break;
                case 'i':
                    bitmask = bitmask ^ (1 << 2);
                    break;
                case 'o':
                    bitmask = bitmask ^ (1 << 1);
                    break;
                case 'u':
                    bitmask = bitmask ^ (1);
                    break;
            }

            if(seenMask[bitmask] == -2) {
                seenMask[bitmask] = i;
            } else {
                maxLen = max(maxLen, i - seenMask[bitmask]);
            }
        }
     
        return maxLen;
    }
};