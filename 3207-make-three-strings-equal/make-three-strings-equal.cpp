#include <algorithm>

class Solution {
public:
    int findMinimumOperations(string s1, string s2, string s3) {
        // Find the longest identical string starting from the right
        // Subtract the length of identical string with all three string
        int shortest_size = min(s1.size(), s2.size());
        int identical_string_size = 0;

        shortest_size = min(shortest_size, (int)s3.size());
        identical_string_size = shortest_size;

        for(int i = 0; i < shortest_size; i++) {
            // cout << s1[i] << " " << s2[i] << " " << s3[i] << endl;
            if(s1[i] != s2[i] || s1[i] != s3[i]) {
                identical_string_size = i;
                break;
            }
        }

        // cout << identical_string_size;
        if(identical_string_size == 0){
            return -1;

        } else {
            int num_operation = 0;
            num_operation += s1.size() - identical_string_size;
            num_operation += s2.size() - identical_string_size;
            num_operation += s3.size() - identical_string_size;
            return num_operation;
        }


    }
};