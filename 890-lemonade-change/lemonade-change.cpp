class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        // We record the number of 5s and 10s bill that we have
        // If customer paid 10$, we deduct 5 from our record
        // if the customer paid 20

        int tens = 0;
        int fives = 0;

        for(int i = 0; i < bills.size(); i++) {
            // cout << tens << " " << fives << endl;
            if(bills[i] == 5) {
                fives++;
            } else if(bills[i] == 10) {
                fives--;
                tens++;
            } else {
                if(tens <= 0) {
                    fives -= 3;
                } else {
                    fives--;
                    tens--;
                }
            }
            if(fives < 0 || tens < 0) return false;
        }
        return true;
    }
};