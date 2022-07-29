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
    ListNode* merge(ListNode* l1, ListNode* l2) {
        ListNode* newList = new ListNode(0);
        ListNode* curr = newList;
        while (l1 != nullptr && l2 != nullptr) {
            if (l1->val > l2->val) {
                curr->next = l2;
                l2 = l2->next;
            } else {
                curr->next = l1;
                l1 = l1->next;
            }
            curr = curr->next;
        }
        
        while (l1 != nullptr) {
            curr->next = l1;
            l1 = l1->next;
            curr = curr->next;
        }
        
        while (l2 != nullptr) {
            curr->next = l2;
            l2 = l2->next;
            curr = curr->next;
        }
        
        ListNode *ans = newList->next;
        // newList->next = nullptr;
        // delete newList;
        return ans;
        
    }

    ListNode* sortList(ListNode* head) {
        if (head == nullptr || head->next == nullptr) {
            return head;
        }
        
        ListNode* last = nullptr;
        ListNode* slow = head;
        ListNode* fast = head;
        
        while (fast != nullptr && fast->next != nullptr) {
            last = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        last->next = nullptr;
        ListNode* l1 = sortList(head);
        ListNode* l2 = sortList(slow);
        
        return merge(l1, l2);
    }
};