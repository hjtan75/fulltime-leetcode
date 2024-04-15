# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        self.num = ''

        def dfs(node):
            self.num += str(node.val)
            if not node.right and not node.left:
                self.res += int(self.num)
                self.num = self.num[:-1]
                return

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            self.num = self.num[:-1]
            return

        if not root:
            return self.res

        dfs(root)
        return self.res