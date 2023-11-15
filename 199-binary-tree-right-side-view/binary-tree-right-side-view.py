# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        arr = []
        self.parser(root, arr, 0)

        return arr

    def parser(self, node, arr, depth):
        if not node:
            return

        if len(arr) <= depth:
            arr.append(node.val)
        else:
            arr[depth] = node.val

        self.parser(node.left, arr, depth+1)
        self.parser(node.right, arr, depth+1)
