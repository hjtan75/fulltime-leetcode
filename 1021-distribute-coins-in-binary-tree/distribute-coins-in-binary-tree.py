# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        # For everynode, we check the current number of coin needed and number of extra coin
        # and the coin that the current node has
        
        def dfs(cur_node, parent):
            if not cur_node:
                return 0

            moves = dfs(cur_node.left, cur_node) + dfs(cur_node.right, cur_node)
            extra_coin = cur_node.val - 1
            parent.val += extra_coin
            moves += abs(extra_coin)
            return moves

        return dfs(root, TreeNode())