# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # Use dfs to get to the leaf of the tree
        # For append the current val into the array and return to the parent
        # before returning, compare both string, choose shorter string, choose lexicographically smaller

        def dfs(node, path, smallest):
            if not node:
                return

            path.append(chr(node.val + ord('a')))

            if not node.left and not node.right:
                curr = ''.join(path[::-1])
                smallest[0] = min(smallest[0], curr)

            dfs(node.left, path, smallest)
            dfs(node.right, path, smallest)

            path.pop()

        smallest = [chr(1 + ord('z'))]

        dfs(root, [], smallest)
        return smallest[0]

            
