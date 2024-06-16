# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.res = None
        def dfs(node):
            if node == None:
                return False

            left = dfs(node.left)
            right = dfs(node.right)

            if node == p or node == q:
                if left or right:
                    self.res = node
                return True

            if left and right:
                self.res = node
                return True

            return left or right

        dfs(root)
        return self.res