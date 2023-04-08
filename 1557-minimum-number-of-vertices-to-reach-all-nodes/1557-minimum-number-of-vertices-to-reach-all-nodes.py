class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        answer = []
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
        
        children = []
        for node in graph:
            children.extend(graph[node])
        
        children = set(children)
        
        for node in graph:
            if node not in children:
                answer.append(node)
                
        return answer