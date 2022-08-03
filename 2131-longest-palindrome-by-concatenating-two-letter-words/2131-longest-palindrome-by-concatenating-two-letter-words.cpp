class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        multiset<string> visited;
        multiset<string> middle;
        set<string>::iterator it;
        int length = 0;
        
        for (int i = 0; i < words.size(); i++) {
            string s = "";
            s.insert(s.end(), words[i][1]);
            s.insert(s.end(), words[i][0]);
            it = visited.find(s);
            
            if (it == visited.end()) {
                visited.insert(words[i]);
                if (words[i][0] == words[i][1]) {
                    middle.insert(words[i]);
                }
            } else {
                visited.erase(it);
                length += 4;
                if (words[i][0] == words[i][1]) {
                    middle.erase(words[i]);
                }
            }
        
        } 
        // cout << middle;
        if (middle.size() >= 1) length += 2;
        return length;
    }
};