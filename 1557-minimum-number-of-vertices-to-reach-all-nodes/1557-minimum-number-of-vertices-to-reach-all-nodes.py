class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
        answer = []
        indegree = [0] * n
        
        for u,v in edges:
            indegree[v] += 1
            
        for idx in range(n):
            if indegree[idx] == 0:
                answer.append(idx)
                
        return answer
    
    
# class Solution:
#     def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        
#         answer = []
#         graph = defaultdict(list)
        
#         for u, v in edges:
#             graph[u].append(v)
        
#         children = []
#         for node in graph:
#             children.extend(graph[node])
        
#         children = set(children)
        
#         for node in graph:
#             if node not in children:
#                 answer.append(node)
                
#         return answer