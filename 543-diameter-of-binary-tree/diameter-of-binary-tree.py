# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.solve(root)
        return self.max_diameter

    def solve(self, node):
        if node == None:
            return 0
        
        l_len = self.solve(node.left)
        r_len = self.solve(node.right)

        self.max_diameter = max(self.max_diameter, l_len + r_len)
        return max(l_len, r_len) + 1