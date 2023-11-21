# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def parsing(node, arr):
            if not node:
                return 
            parsing(node.left, arr)
            arr.append(node.val)
            parsing(node.right, arr)

        parsing(root, arr)
        return arr[k-1]