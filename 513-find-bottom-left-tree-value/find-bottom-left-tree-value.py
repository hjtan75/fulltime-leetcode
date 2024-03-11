# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        # Use dfs to parse down the tree
        # When parsing down mark the depth
        # If we use dfs, the leftmost value will be mark first
        # Unless, there is a deeper value, the leftmost value will remain on top
        self.deepest, self.res = 0, 0

        def dfs(node, depth):
            if not node:
                return 
            
            if depth > self.deepest:
                self.deepest = depth
                self.res = node.val
        
            dfs(node.left, depth+1)
            dfs(node.right, depth+1)

            return 
        
        dfs(root, 1)
        return self.res

        
        