class Solution {
public:
    string multiply(string num1, string num2) {
        string ans;
        vector<int> cal(405);
        
        if (num1.size() < num2.size())  swap(num1, num2);
        reverse(num1.begin(), num1.end());
        reverse(num2.begin(), num2.end());
        
        for (int i = 0; i < num2.size(); i++) {
            int carryOver = 0;
            for (int j = 0; j < num1.size(); j++) {
                int first = num1[j] - '0';
                int second = num2[i] - '0';
                int mul = (first * second) + carryOver;
                
                mul += cal[i + j] ;
                cal[i + j] = mul % 10;
                mul /= 10;
                int carry_index = 1;
                while (mul > 0) {
                    cal[i + j + carry_index] += mul % 10;
                    mul /= 10;
                }
                
            }
        }
        
        for (int i = 0; i < cal.size(); i++) {
            int current = cal[i];
            int idx = 1;
            ans.insert(ans.begin(), (current % 10) + '0');
            current /= 10;
            
            while (current > 0) {
                cal[i + idx] += current % 10;
                current /= 10;
            }
        }
        
        int last_zero = 0;
        for (int i = 0; i < ans.size(); i++) {
            if (ans[i] != '0') break;
            last_zero++;
        }
        
        ans.erase(0, last_zero);
        if (ans.size() == 0) return "0";
        return ans;
    }
};