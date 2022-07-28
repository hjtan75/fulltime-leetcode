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
    ListNode* reverseList(ListNode* head) {
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        if (head->next->next == nullptr) {
            head->next->next = head;
            head = head->next;
            head->next->next = nullptr;
            return head;
        }
        
        ListNode* pre = head;
        ListNode* cur = head->next;
        ListNode* nex = head->next->next;
        
        while (nex != nullptr) {
            cur->next = pre;
            pre = cur;
            cur = nex;
            nex = nex->next;
        }
        cur->next = pre;
        head->next = nullptr;
        head = cur;
        return head;
    }
};