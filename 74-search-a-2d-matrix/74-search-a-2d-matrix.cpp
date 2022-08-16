class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int num_row = matrix.size();
        int num_col = matrix[0].size();
        
        int i = num_col - 1;
        int j = 0;
        
        while (i >= 0 && j < num_row) {
            if (matrix[j][i] == target) return true;
            if (matrix[j][i] > target) i--;
            else j++;
        }
        
        return false;
    }
};