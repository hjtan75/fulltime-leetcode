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
        if (head->next == nullptr) return true;
        
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* midpoint = nullptr;
        
        while(fast != nullptr && fast->next != nullptr) {
            // midpoint = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        // Reverse first half of linked list
        ListNode dummy;
        ListNode* a = &dummy;
        ListNode* b = head;
        ListNode* c = head->next;
        
        while (b != slow) {
            b->next = a;
            a = b;
            b = c;
            c = c->next;
        }
        head->next = nullptr;
        head = a;
        
        ListNode* p1 = head;
        ListNode* p2 = slow;
        if (fast != nullptr) p2 = p2->next;
        while (p1 != nullptr && p2 != nullptr) {
            cout << p1->val << " " << p2->val << endl;
            if (p1->val != p2->val) return false;
            p1 = p1->next;
            p2 = p2->next;
        }
        return true;
        
        
    }
};