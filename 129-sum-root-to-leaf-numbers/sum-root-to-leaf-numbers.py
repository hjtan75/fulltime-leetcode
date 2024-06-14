# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Use dfs to parse down the three, in every non lead node we append the value to an array
        # On the leaf node cast the the number to an integer and return the number 
        # on every return in then non leaf node, add the value from right and left child then return

        def dfs(node, arr):
            if node.left == None and node.right == None:
                res = 0
                for val in arr:
                    res *= 10
                    res += val

                res *= 10
                res += node.val
                return res

            left = 0
            right = 0
            arr.append(node.val)
            if node.left:
                left = dfs(node.left, arr)
            if node.right:
                right = dfs(node.right, arr)

            arr.pop()
            return left + right

        return dfs(root, [])