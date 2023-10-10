# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.dfs(root, subRoot):
            return True

        if not root:
            return False

        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r

    def dfs(self, root, subRoot):
        if not root and not subRoot:
            return True
        
        if (not root or not subRoot) or root.val != subRoot.val:
            return False

        return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)