# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.ans = -1001
        
        def parse(node):
            if not node:
                return -1001

            l_val = parse(node.left)
            r_val = parse(node.right)
            c_max = max(l_val, r_val, l_val + r_val, 0) + node.val
            self.ans = max(self.ans, c_max)
           
            return max(l_val, r_val, 0) + node.val

        parse(root)
        return self.ans