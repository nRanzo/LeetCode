"""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

class Solution:
    # iterative bfs
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        visited = {node: Node(node.val)}
        q = deque([node])

        while q:
            curr = q.popleft()      # using pop() would be dfs
            for nei in curr.neighbors:
                if nei not in visited:
                    visited[nei] = Node(nei.val)
                    q.append(nei)
                visited[curr].neighbors.append(visited[nei])

        return visited[node]