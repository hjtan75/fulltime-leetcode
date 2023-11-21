# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.parse(root, -2**31 - 1, 2**31)
    
    def parse(self, node, minimum, maximum):
        if not node:
            return True

        if node.val <= minimum or node.val >= maximum:
            return False
        else:
            return self.parse(node.left, minimum, node.val) and self.parse(node.right, node.val, maximum)