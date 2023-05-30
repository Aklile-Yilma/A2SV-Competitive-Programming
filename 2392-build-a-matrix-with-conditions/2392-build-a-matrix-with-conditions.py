class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        #(node, (row, col)) = (node, (-1, -1))
        
        def topSort(graph, indegree):
            
            q = deque()
            # get independent nodes
            for node in range(1, k+1):
                if indegree[node] == 0:
                    q.append(node)
                    
            order = {}
            pos = 0
            
            while q:
                node = q.popleft()
                order[node] = pos
                pos += 1
                
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        q.append(child)
                        
            return order
            
        #sort by column
        col_graph = [[] for _ in range(k+1)]
        col_indegree = [0] * (k+1)
        
        for u, v in colConditions:
            col_graph[u].append(v)
            col_indegree[v] += 1
            
        col_sort = topSort(col_graph, col_indegree)
        
        if len(col_sort) != k:
            return []

        #sort by row
        row_graph = [[] for _ in range(k+1)]
        row_indegree = [0] * (k+1)
        
        for u, v in rowConditions:
            row_graph[u].append(v)
            row_indegree[v] += 1
            
        row_sort = topSort(row_graph, row_indegree)
        
        if len(row_sort) != k:
            return []
                    
        #build matrix
        mat = [[0]*k  for _ in range(k)]       
        
        for node in range(1, k+1):
            row, col = row_sort[node], col_sort[node]
            mat[row][col] = node
            
            
        return mat