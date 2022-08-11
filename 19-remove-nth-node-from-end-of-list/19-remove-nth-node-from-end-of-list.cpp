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
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        int num_node = 0;
        
        ListNode* ptr = head;
        while(ptr != nullptr) {
            ptr = ptr->next;
            num_node++;
        }
        
        ptr = head;
        for (int i = 0; i < num_node - n - 1; i++) {
            ptr = ptr->next;
        }
        
        if (num_node == n) {
            return head->next;
        }
        ListNode* to_be_deleted = ptr->next;
        ListNode* next = to_be_deleted->next;
        ptr->next = next;
        delete to_be_deleted;
        
        return head;
    }
};