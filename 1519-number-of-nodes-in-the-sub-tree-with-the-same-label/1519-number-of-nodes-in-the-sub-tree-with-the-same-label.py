class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        
        graph = [[] for _ in range(n)]
        counts = [0] * n
        
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        def dfs(node, parent):
            
            letters_count = Counter()
            for child in graph[node]:
                if child != parent:
                    letters_count +=  dfs(child, node)
                
            letters_count[labels[node]] += 1
            counts[node] = letters_count[labels[node]]
            
            return letters_count
        
        dfs(0, -1)

        return counts
            
        