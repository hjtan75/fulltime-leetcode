# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return self.depthExplorer(root)

    def depthExplorer(self, node) -> int:
        if node:
            return max(self.depthExplorer(node.left), self.depthExplorer(node.right))+1
        else:
            return 0