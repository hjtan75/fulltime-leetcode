class Solution {
public:
    vector<string> uncommonFromSentences(string s1, string s2) {
        unordered_map<string, int> s1WordFreq, s2WordFreq;

        stringstream ss1(s1);
        stringstream ss2(s2);
        string word;
        unordered_map<string, int>::iterator ptr;
        vector<string> ans;

        while(ss1 >> word) {
            if(s1WordFreq.contains(word)) {
                s1WordFreq[word]++;
            } else {
                s1WordFreq[word] = 1;
            }
        }

        while(ss2 >> word) {
            if(s2WordFreq.contains(word)) {
                s2WordFreq[word]++;
            } else {
                s2WordFreq[word] = 1;
            }
        }

        for (ptr = s1WordFreq.begin(); ptr != s1WordFreq.end(); ++ptr) {
            if(ptr->second == 1 && !s2WordFreq.contains(ptr->first)) {ans.push_back(ptr->first);}
        }

        for (ptr = s2WordFreq.begin(); ptr != s2WordFreq.end(); ++ptr) {
            if(ptr->second == 1 && !s1WordFreq.contains(ptr->first)) {ans.push_back(ptr->first);}
        }

        return ans;
    }
};