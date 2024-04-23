class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # The brute force method would be trying every possible root 
        # For every possible root, find out the depth of the tree

        # The solution is to use a minimum spanning tree (MST) to find the root for MHT
        # We are trimming of the leave until the last/last two node 
        # Those are the root for MHT
        # There can be only <= 2 roots, because if there are tree root, the center would be 
        # the new root
        # Create an adjacent list and array to record degree by each vertices.
        # Remove the vertices which has degree of one
        # Add those into a deque
        # Keep removing leaves until, only 2/1 vertices left

        if n == 1:
            return [0]

        adjacent_list = {}
        degree = [0] * n

        for u, v in edges:
            if u not in adjacent_list:
                adjacent_list[u] = set()

            if v not in adjacent_list:
                adjacent_list[v] = set()

            adjacent_list[u].add(v)
            adjacent_list[v].add(u)
            degree[u] += 1
            degree[v] += 1

        leaves = deque([idx for idx, val in enumerate(degree) if val == 1])
        # print(degree)
        # print(leaves)
        while len(adjacent_list) > 2:
            num_leaves = len(leaves)
            for _ in range(num_leaves):
                leaf = leaves.popleft()
                for parent in adjacent_list[leaf]:
                    leaf_parent = adjacent_list[leaf]
                    adjacent_list[parent].remove(leaf)
                    degree[parent] -= 1
                    if degree[parent] == 1:
                        leaves.append(parent)

                del adjacent_list[leaf]

        return list(leaves)