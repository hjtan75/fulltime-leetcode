# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # pass down min and max value from accestor with dfs
        # Compare min, max with current node value
        # update min, max and largest different 
        # Return largest different

        return self.dfs(root, root.val, root.val)

    def dfs(self, node, maxi, mini):
        if not node:
            return abs(maxi-mini)

        maxi = max(maxi, node.val)
        mini = min(mini, node.val)

        return max(self.dfs(node.left, maxi, mini), self.dfs(node.right, maxi, mini))
        


        