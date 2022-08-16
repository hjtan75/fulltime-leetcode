/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int pathSum(TreeNode* root, int targetSum) {
        long long ans = 0;
        solve(root, targetSum, ans);
        
        return ans;
    }
    
    void solve(TreeNode* root, int targetSum, long long &num_path) {
        if (root == nullptr) return;
        
        bfs(root, targetSum, 0, num_path);
        if (root->left != nullptr) solve(root->left, targetSum, num_path);
        if (root->right != nullptr) solve(root->right, targetSum, num_path);
        
    }
    
    void bfs(TreeNode *node, int targetSum, long long sum, long long &num_path) {
        if (node == nullptr) return;
        
        long long total = (long long)node->val + sum;
        if (total == targetSum) num_path++;
        bfs(node->left, targetSum, total, num_path);
        bfs(node->right, targetSum, total, num_path);
    }
};