class Solution {
public:
    int findMin(vector<int>& nums) {
        int left = 0;
        int right = nums.size() - 1;
        int mid;
        
        while (right > left) {
            mid = (left + right) / 2;
            if (nums[mid] >= nums[0]) {
                left = mid + 1;
            } else {
                right = mid;
            }
        
        }
        if (nums[left] > nums[0]) return nums[0];
        return nums[left];
    }
};