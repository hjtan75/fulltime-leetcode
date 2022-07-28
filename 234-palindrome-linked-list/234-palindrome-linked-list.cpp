/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    bool isPalindrome(ListNode* head) {
        vector<int> arr;
        ListNode* ptr = head;
        int num = 0;
        
        while(ptr != nullptr) {
            arr.push_back(ptr->val);
            ptr = ptr->next;
            num++;
        }
        
        int p1, p2;
        if (num % 2 == 0) {
            p1 = num / 2 - 1;
            p2 = num / 2;
        } else {
            p1 = num / 2;
            p2 = num / 2;
        }
        
        while (p1 >= 0 && p2 < num) {
            if (arr[p1] != arr[p2]) return false;
            p1--;
            p2++;
        }
        return true;
    }
};