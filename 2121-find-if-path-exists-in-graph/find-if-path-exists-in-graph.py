class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # The currently i can think of is the grouping feature
        # I forgot what it's called, but the idea is a tree like structure
        # If you find link between two node, merge the tree
        # If you find out wheter they are the same group, find the parents.
        # TC: O(n*m), n: edges, m: nodes
        # MC: O(m)
        arr = [-1] * n
        depth = [1] * n
        def identify(a, b):
            if find_parent(a) == find_parent(b):
                return True
            else:
                return False

        def merge(a, b):
            parent_a = find_parent(a)
            parent_b = find_parent(b)
            if parent_a != parent_b:
                if depth[parent_a] > depth[parent_b]:  
                    arr[parent_b] = parent_a
                elif depth[parent_b] > depth[parent_a]:
                    arr[parent_a] = parent_b
                else:
                    arr[parent_b] = parent_a
                    depth[parent_a] += 1
            return

        def find_parent(a):
            while arr[a] != -1:
                a = arr[a]
            return a

        for s, d in edges:
            merge(s, d)

        # print(arr)
        # print(depth)
        return identify(source, destination)
