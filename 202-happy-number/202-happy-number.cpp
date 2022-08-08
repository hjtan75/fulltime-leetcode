class Solution {
public:
    bool isHappy(int n) {
        set<int> visited;
        
        while (n != 1 && visited.find(n) == visited.end()) {
            int ans = 0;
            visited.insert(n);
            while (n > 0) {
                int num = n % 10;
                n /= 10;
                ans += num * num;
            }
            
            n = ans;
        }
        
        if (n == 1) return true;
        return false;
    }
};