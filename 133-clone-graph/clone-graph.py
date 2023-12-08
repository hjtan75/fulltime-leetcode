"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        def spanningTree(new_node, old_node):
            for old_neighbor in old_node.neighbors:
                if old_neighbor.val not in created:
                    # Create a new node if not created
                    # Add current node to created node's neighbor
                    create_node = Node(old_neighbor.val, [])
                    created[create_node.val] = create_node
                    new_node.neighbors.append(create_node)
                    spanningTree(create_node, old_neighbor)
                else:
                    # Add current node to created node's neighbor
                    # created[old_neighbor.val].neighbors.append(new_node)
                    new_node.neighbors.append(created[old_neighbor.val])

            return
            
        if node == None:
            return None

        
        new_head = Node(node.val)
        created = {1:new_head}
        spanningTree(new_head, node)
        return new_head
        