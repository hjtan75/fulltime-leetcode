class Solution {
public:
    int removeElement(vector<int>& nums, int val) {
        // This one should be easy
        // The are two pointer, the first is the find the element that is equal to val
        // The next element is not equal to k
        // Then swap these two element.

        if(nums.size() == 0) {
            return 0;
        }

        int left = 0;
        int right = nums.size() - 1;

        while(right >= 0 && nums[right] == val) {
            right--;
        }

        if(right < 0) {
            return 0;
        }

        while(left <= right) {
            if(nums[left] == val) {
                int tmp = nums[right];
                nums[right] = nums[left];
                nums[left] = tmp;
                while(nums[right] == val) {
                    right--;
                }
            }
            left++;
        }

        return left;
    }
};