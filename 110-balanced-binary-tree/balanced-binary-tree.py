# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if self.depthExplorer(root) > 0:
            return True
        else:
            return False

    def depthExplorer(self, node) -> int:
        if node:
            lHeight = self.depthExplorer(node.left)
            rHeight = self.depthExplorer(node.right)
            
            if abs(lHeight-rHeight) > 1 or lHeight < 0 or rHeight < 0:
                return -1
            else:
                return max(lHeight, rHeight) + 1
        else:
            return 0