# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        num = []

        def dfs(node):
            num.append(node.val)
            if not node.right and not node.left:
                s = ''.join(map(str, num))
                print(s)
                self.res += int(s)
                num.pop()
                return

            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)
            num.pop()
            return

        if not root:
            return self.res

        dfs(root)
        return self.res