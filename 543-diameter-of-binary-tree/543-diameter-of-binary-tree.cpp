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
    int diameterOfBinaryTree(TreeNode* root) {
        int max_diameter = 0;
        int depth = 0;
        
        solve(root, depth, max_diameter);
        return max_diameter;
    }
    
    int solve(TreeNode* node, int depth, int &max_diameter) {
        if (node == nullptr) return 0;
        
        int left = solve(node->left, depth, max_diameter);
        int right = solve(node->right, depth, max_diameter);
        max_diameter = max(max_diameter, left + right);
        return max(left, right) + 1;
    }
    
};