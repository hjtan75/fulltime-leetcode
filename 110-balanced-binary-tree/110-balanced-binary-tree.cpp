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
    bool isBalanced(TreeNode* root) {
        if (root == nullptr) return true;
        bool flag = true;
        solve(root, 1, flag);
        
        return flag;
    }
    
    int solve(TreeNode* node, int height, bool &flag) {
        if (node == nullptr) return height - 1;
        int left_max = solve(node->left, height + 1, flag);
        int right_max = solve(node->right, height + 1, flag);
        
        if (abs(left_max - right_max) > 1) flag = false;
        return max(left_max, right_max);
    }
};