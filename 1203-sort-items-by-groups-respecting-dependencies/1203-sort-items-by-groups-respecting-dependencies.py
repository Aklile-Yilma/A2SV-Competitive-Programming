class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        
        def topSort(nodes, graph, indegree):
            q = deque()
            
            for node in nodes:
                if indegree[node] == 0:
                    q.append(node)
                    
            order = []
            while q:
                node = q.popleft()
                order.append(node)
                for child in graph[node]:
                    indegree[child] -= 1
                    if indegree[child] == 0:
                        q.append(child)
           
            
            return order
        
        group_items = defaultdict(list)
        
        #collect items by groups
        for node in range(n):
            if group[node] == -1:
                group[node] = m + node
                
            group_items[group[node]].append(node)
                
        graph_item = defaultdict(list)
        indegree_item = defaultdict(int)
        #build graph within the group
        for u, v_list in enumerate(beforeItems):
            for v in v_list:
                if group[u] == group[v]:
                    graph_item[v].append(u)
                    indegree_item[u] += 1
                    
        #topsort within groups
        order_items = {}
        for group_id in group_items:
            sorted_items = topSort(group_items[group_id], graph_item, indegree_item)
            if len(sorted_items) != len(group_items[group_id]):
                return []
            
            order_items[group_id] = sorted_items
            
        #build group graph
        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)

        for u, v_list in enumerate(beforeItems):
            for v in v_list:
                if group[u] != group[v]:
                    group_graph[group[v]].append(group[u])
                    group_indegree[group[u]] += 1

        groups = set(group)
        #topsort across groups
        sorted_groups = topSort(groups, group_graph, group_indegree)
        if len(groups) != len(sorted_groups):
            return []

        ans = []
        for group_id in sorted_groups:
            ans.extend(order_items[group_id])

        return ans



        
        
                    
        
                    
        
                
                
        
        