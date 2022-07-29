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

void merge(vector<int> &arr, int left, int mid, int right) {
    int numOfElement = right - left + 1;
    vector<int> newArr(numOfElement, 0);
    int leftIdx = left;
    int rightIdx = mid + 1;
    int newArrIdx = 0;
    
    while (newArrIdx < numOfElement && leftIdx <= mid && rightIdx <= right) {
        if (arr[leftIdx] > arr[rightIdx]) {
            newArr[newArrIdx] = arr[rightIdx];
            rightIdx++;
        } else {
            newArr[newArrIdx] = arr[leftIdx];
            leftIdx++;
        }
        newArrIdx++;
    }
    
    while (leftIdx <= mid) {
        newArr[newArrIdx] = arr[leftIdx];
        leftIdx++;
        newArrIdx++;
    }
    
    while (rightIdx <= right) {
        newArr[newArrIdx] = arr[rightIdx];
        rightIdx++;
        newArrIdx++;
    }
    
    newArrIdx = 0;
    for (int i = left; i <= right; i++) {
        arr[i] = newArr[newArrIdx];
        newArrIdx++;
    }
}

void mergesort(vector<int> &arr, int left, int right) {
    if (left >= right) return;
    int mid = (left + right) / 2;
    mergesort(arr, left, mid);
    mergesort(arr, mid+1, right);
    merge(arr, left, mid, right);
}


class Solution {
public:
    ListNode* sortList(ListNode* head) {
        vector<int> arr;
        ListNode *ptr = head;
        
        while (ptr != nullptr) {
            arr.push_back(ptr->val);
            ptr = ptr->next;
        }
        
        // Merge sort
        mergesort(arr, 0, arr.size() - 1);
        ptr = head;
        for (int i = 0; i < arr.size(); i++) {
            ptr->val = arr[i];
            ptr = ptr->next;
        }
        
        return head;
        
    }
};