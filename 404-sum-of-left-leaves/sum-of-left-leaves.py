# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        def dfs(node, direction):
            if not node:
                return

            if not node.left and not node.right and direction == 1:
                self.res += node.val
                return

            dfs(node.left, 1)
            dfs(node.right, 2)
            return 

        self.res = 0
        dfs(root, 0)
        return self.res