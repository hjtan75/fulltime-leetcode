class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        vector<int> counts(26, 0);
        priority_queue<int> pq;
        deque<pair<int, int>> dq;
        
        for (int i = 0; i < tasks.size(); i++) {
            counts[tasks[i] - 'A']++;
        }
        
        for (int i = 0; i < counts.size(); i++) {
            if (counts[i] > 0) pq.push(counts[i]);
        }
        
        int time = 0;
        while (!pq.empty() || !dq.empty()) {
            time++;
            
            if (!pq.empty()) {
                if (pq.top() > 1) {
                    dq.push_back(pair<int, int>(pq.top() - 1, time + n));
                }
                pq.pop();
            }
            
            if (!dq.empty() && dq.front().second == time) {
                pq.push(dq.front().first);
                dq.pop_front();
            }
        }
        return time;
    }
};