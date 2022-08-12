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
    ListNode* sortList(ListNode* head) {
        if (head == nullptr) return nullptr;
        if (head->next == nullptr) return head;
        ListNode* slow = head;
        ListNode* fast = head;
        ListNode* temp = nullptr;
        
        while (fast != nullptr && fast->next != nullptr) {
            temp = slow;
            slow = slow->next;
            fast = fast->next->next;
        }
        
        temp->next = nullptr;
        ListNode* list1 = sortList(head);
        ListNode* list2 = sortList(slow);
        ListNode* merged = merge(list1, list2);
        return merged;
    }
    
    ListNode* merge(ListNode* list1, ListNode* list2) {
        ListNode dummy(0);
        ListNode* ptr = &dummy;
        
        while(list1 != nullptr && list2 != nullptr) {
            if (list1->val <= list2->val) {
                ptr->next = list1;
                list1 = list1->next;
            } else {
                ptr->next = list2;
                list2 = list2->next;
            }
            ptr = ptr->next;
        }
        
        while (list1 != nullptr) {
            ptr->next = list1;
            list1 = list1->next;
            ptr = ptr->next;
        }
        
        while (list2 != nullptr) {
            ptr->next = list2;
            list2 = list2->next;
            ptr = ptr->next;
        }
        
        return dummy.next;
    }
};