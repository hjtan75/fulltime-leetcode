class Solution {
public:
    vector<int> findWordsContaining(vector<string>& words, char x) {
        vector<int> ans;
        for(int i = 0; i < words.size(); i++) {
            for(int l = 0; l < words[i].size(); l++) {
                if(x == words[i][l]) {
                    ans.push_back(i);
                    break;
                }
            }
        }
        return ans;
    }
};