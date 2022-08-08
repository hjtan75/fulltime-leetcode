class Solution {
public:
    vector<int> spiralOrder(vector<vector<int>>& matrix) {
        int direction = 0;
        int i = 0, j = 0;
        int maxCol = matrix[0].size() - 1;
        int maxRow = matrix.size() - 1;
        int minCol = 0;
        int minRow = 0;
        vector<int> ans;
        
        while (ans.size() < matrix[0].size() * matrix.size()) {
            if (direction == 0) {
                if (i > maxCol) {
                    minRow++;
                    i--;
                    j++;
                    direction = 1;
                    continue;
                }
                ans.push_back(matrix[j][i]);
                i++;
            } else if (direction == 1) {
                if (j > maxRow) {
                    maxCol--;
                    i--;
                    j--;
                    direction = 2;
                    continue;
                }
                ans.push_back(matrix[j][i]);
                j++;
            } else if (direction == 2) {
                if (i < minCol) {
                    maxRow--;
                    i++;
                    j--;
                    direction = 3;
                    continue;
                }
                ans.push_back(matrix[j][i]);
                i--;
            } else {
                if (j < minRow) {
                    minCol++;
                    i++;
                    j++;
                    direction = 0;
                    continue;
                }
                ans.push_back(matrix[j][i]);
                j--;
            } 
        }
        
        return ans;
        
    }
};