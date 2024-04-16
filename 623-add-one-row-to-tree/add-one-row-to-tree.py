# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        # Pass through depth in dfs
        # If dfs depth == 1, create new root, otherwise create a node with the subtree added to it
        self.val = val
        self.depth = depth

        def dfs(node, curr_depth):
            if not node:
                return

            if curr_depth == self.depth - 1:
                left = TreeNode(self.val, left=node.left)
                right = TreeNode(self.val, right=node.right)
                node.left = left
                node.right = right
                return

            dfs(node.left, curr_depth + 1)
            dfs(node.right, curr_depth + 1)
            return 

        if depth == 1:
            newRoot = TreeNode(self.val, left=root)
            return newRoot
        else:
            dfs(root, 1)
            return root
            
            