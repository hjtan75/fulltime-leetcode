class Solution {
public:
    bool isPalindrome(int x) {
        vector<int> arr;

        if(x < 0) return false;

        while(x > 0) {
            int digit = x % 10;
            x = floor(x/10);
            arr.push_back(digit);
        }

        int l = 0;
        int r = arr.size() - 1;

        while(l < r) {
            if(arr[l] != arr[r]) {
                return false;
            }
            l++;
            r--;
        }

        return true;
    }
};