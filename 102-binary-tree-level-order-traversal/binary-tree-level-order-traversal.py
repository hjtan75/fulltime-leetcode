# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        array = []
        self.traversal(root, array, 0)
        
        return array

    def traversal(self, node, arr, depth):
        if not node:
            return
        if len(arr) <= depth:
            arr.append(list())

        arr[depth].append(node.val)
        self.traversal(node.left, arr, depth+1)
        self.traversal(node.right, arr, depth+1)