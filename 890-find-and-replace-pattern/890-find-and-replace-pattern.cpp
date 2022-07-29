class Solution {
public:
    vector<string> findAndReplacePattern(vector<string>& words, string pattern) {
        vector<string> ans;
        for (int w = 0; w < words.size(); w++) {
            vector<int> transform(26, -26);
            vector<bool> patternFlag(26, true);
            int c = pattern.size();
            
            for (int i = 0; i < pattern.size(); i++) {
                if (transform[words[w][i] - 'a'] < -25 && patternFlag[pattern[i] - 'a']) {
                    // New word
                    transform[words[w][i] - 'a'] = words[w][i] - pattern[i];
                    patternFlag[pattern[i] - 'a'] = false;
                } else {
                    if (pattern[i] + transform[words[w][i] - 'a'] != words[w][i]) {
                        cout << "Break for " << words[w] << endl;
                        break;
                    }
                }
                c--;
            }
            if (c == 0) ans.push_back(words[w]);
        }
        
        return ans;
    }
};