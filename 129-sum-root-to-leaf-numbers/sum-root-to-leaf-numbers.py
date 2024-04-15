# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0

        def dfs(node, path_sum):
            path_sum = path_sum * 10 + node.val
            if not node.right and not node.left:
                self.res += path_sum
                path_sum /= 10
                return

            if node.left:
                dfs(node.left, path_sum)
            if node.right:
                dfs(node.right, path_sum)
            path_sum /= 10
            return

        if not root:
            return self.res

        dfs(root, 0)
        return self.res