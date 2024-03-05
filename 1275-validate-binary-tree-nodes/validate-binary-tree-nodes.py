class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        # Based on the number of node and leftchild and rightchild given
        # Determine if the tree is a binary tree
        # Cases to be aware of:
        # 1. A node with two differente parent
        # 2. Cycle
        # 3. Two different distinct tree
        # 4. Root may not start at zero
        # Problem 1 and 2 can be solve with visited array
        # Problem 3 and 4 can be solve with passing root that haven't been parse
        # size valid root should be 1 larger tha main_tree_valid_root because there is only one true root
        # Time O(n) dfs
        # Memory O(1)

        visited = [False] * n
        valid_root, not_true_root = [], []

        def dfs(node):
            if node == -1:
                return True
            if visited[node]:
                if node in valid_root:
                    not_true_root.append(node)
                    return True
                else:
                    return False
            visited[node] = True
            return dfs(leftChild[node]) & dfs(rightChild[node])


        for i in range(n):
            if not visited[i]:
                validity = dfs(i)
                if not validity:
                    return False
                else:
                    valid_root.append(i)
        
        if len(valid_root) - len(not_true_root) == 1:
            return True
        else:
            return False
