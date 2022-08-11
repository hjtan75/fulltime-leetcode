class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        string same = strs[0];
        int idx;
        
        for (int i = 0; i < strs.size(); i++) {
            idx = 0;
            while(idx < strs[i].size() && idx < same.size()) {
                if (strs[i][idx] != same[idx]) {
                    same.resize(idx);
                    break;
                }
                idx++;
            }
            same.resize(idx);
        }
        
        return same;
    }
};