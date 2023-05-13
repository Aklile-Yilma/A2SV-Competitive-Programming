from typing import List


class Solution:
    # Function to detect cycle in an undirected graph.
    def isCycle(self, V: int, adj: List[List[int]]) -> bool:
        # Code here

        def dfs(node, parent):

            visited.add(node)
            for child in adj[node]:
                if child == parent:
                    continue
                # found cycle
                if child in visited:
                    return True
                if dfs(child, node):
                    return True

            return False

        visited = set()
        for node in range(v):
            if node not in visited:
                if dfs(node, -1):
                    return 1

        return 0
