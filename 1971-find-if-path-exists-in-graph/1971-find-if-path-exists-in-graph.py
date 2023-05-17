class Solution:
    
    def build(self, n):
        self.n = 0
        self.root = [node for node in range(n)]
        self.size = [1 for _ in range(n)]
        
    def find(self, x):
        #hold x
        hold = x
        while self.root[x] != x:
            x = self.root[x]
            
        #path compression
        #x is now the root, i didn't reach the root
        while x != self.root[hold]:
            temp = self.root[hold]
            #change root of node
            self.root[hold] = x
            hold = temp
            
        return x
            
    def union(self, x, y):
        root1 = self.find(x)
        root2 = self.find(y)
        size1 = self.size[root1]
        size2 = self.size[root2]
        
        if size1 <= size2:
            self.root[root2] = root1
            self.size[root1] += root2
        else:
            self.root[root1] = root2
            self.size[root2] += root1
            
    def connected(self, x, y):
        return self.find(x) == self.find(y)
        
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        self.build(n)
        self.n = n
        
        for u, v in edges:
            self.union(u, v)
            
        return self.connected(source, destination) 

#dfs
# class Solution:
#     def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        
#         graph = defaultdict(list)
#         #build adjacency list
#         for edge in edges:
#             u, v = edge
#             graph[u].append(v)
#             graph[v].append(u)
            
#         def dfs(node, visited):
            
#             if node == destination:
#                 return True
            
#             visited.add(node)
#             for neighbor in graph[node]:
#                 if neighbor not in visited:
#                     found = dfs(neighbor, visited)
#                     if found:
#                         return True
#             return False
        
#         return dfs(source, set())
            