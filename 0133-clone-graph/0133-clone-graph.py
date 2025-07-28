"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    # bfs
    def __init__(self):
        self.neighborhood = {}
    
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        if node in self.neighborhood:
            return self.neighborhood[node]

        clone = Node(node.val)
        self.neighborhood[node] = clone
        for n in node.neighbors:
            clone.neighbors.append(self.cloneGraph(n))
        return clone