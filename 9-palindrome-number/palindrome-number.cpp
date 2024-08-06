class Solution {
public:
    bool isPalindrome(int x) {
        if(x < 0) return false;

        long x_copy = x;
        long x_reversed = 0;

        while(x > 0) {
            x_reversed = (x_reversed * 10) + (x % 10);
            x = floor(x/10);
        }

        return x_copy == x_reversed;
    }
};