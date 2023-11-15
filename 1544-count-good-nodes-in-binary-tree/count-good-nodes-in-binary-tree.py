# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res = 1
        return self.parser(root, root.val, res)
        

    def parser(self, node, cur_max, res):
        if not node:
            return 0 

        flag = 0
        if node.val >= cur_max:
            flag += 1

        cur_max = max(cur_max, node.val)

        return self.parser(node.left, cur_max, res) + self.parser(node.right, cur_max, res) + flag