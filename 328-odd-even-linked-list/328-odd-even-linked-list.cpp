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
    ListNode* oddEvenList(ListNode* head) {
        if (head == nullptr || head->next == nullptr || head->next->next == nullptr) {
            return head;
        }
        
        ListNode* oddTail = head;
        ListNode* evenHead = head->next;
        ListNode* evenTail = head->next;
        ListNode* cur = head->next->next;
        int count = 3;
        
        while (cur != nullptr) {
            if (count % 2 == 0) {
                evenTail->next = cur;
                evenTail = cur;
            } else {
                oddTail->next = cur;
                oddTail = cur;
            }
            cur = cur->next;
            count++;
        }
        
        evenTail->next = nullptr;
        oddTail->next = evenHead;
        return head;
        
    }
};