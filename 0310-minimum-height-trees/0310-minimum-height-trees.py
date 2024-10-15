class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        # constructing tree and leaves queue
        adj_list = defaultdict(list)
        degree = [0] * n
        for a, b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)
            degree[a] += 1
            degree[b] += 1
        leaves = deque([i for i in range(n) if degree[i] == 1])

        # remove leaves
        remaining_nodes = n
        while remaining_nodes > 2:
            leaves_count = len(leaves)
            remaining_nodes -= leaves_count
            for _ in range(leaves_count):
                leaf = leaves.popleft()
                for neighbor in adj_list[leaf]:
                    degree[neighbor] -= 1
                    if degree[neighbor] == 1:
                        leaves.append(neighbor)
        return list(leaves)