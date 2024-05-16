# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(node):
            if not node.left and not node.right:
                if node.val == 0:
                    return False
                else:
                    return True

            left = dfs(node.left)
            right = dfs(node.right)

            if node.val == 2:
                return left | right
            else:
                return left & right


        return dfs(root) 