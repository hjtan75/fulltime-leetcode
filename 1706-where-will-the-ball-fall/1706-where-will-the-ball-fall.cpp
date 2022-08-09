class Solution {
public:
    vector<int> findBall(vector<vector<int>>& grid) {
        int maxCol = grid[0].size();
        int maxRow = grid.size();
        vector<int> ans(maxCol);
        
        for (int i = 0; i < maxCol; i++) {
            int x = i;
            for (int j = 0; j < maxRow; j++) {
                if (x > 0 && grid[j][x - 1] == 1 && grid[j][x] == -1) {
                    x = -1;
                    break;
                }
                
                if (x < maxCol - 1 && grid[j][x] == 1 && grid[j][x + 1] == -1) {
                    x = -1;
                    break;
                }
                
                
                if (grid[j][x] == 1) x++;
                else x--;
                
                if (x >= maxCol || x < 0) {
                    x = -1;
                    break;
                }
            }
            
            ans[i] = x;
        }
        
        
        return ans;
    }
};