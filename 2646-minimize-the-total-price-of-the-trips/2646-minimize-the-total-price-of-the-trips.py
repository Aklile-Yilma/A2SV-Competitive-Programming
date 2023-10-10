class Solution:
    def minimumTotalPrice(self, n: int, edges: List[List[int]], price: List[int], trips: List[List[int]]) -> int:
        
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
         
        count = [0] * n
        def dfs_count(parent, node):
            
            nonlocal count
            if node == dst:
                count[node] += 1
                return True
            
            for child in graph[node]:
                if child != parent:
                    if dfs_count(node, child):
                        count[node] += 1
                        return True
                        
            return False
        
        for trip in trips:
            src, dst = trip
            dfs_count(-1, src)
            
        """
        node: halfed, non-halfed
        0 -> 1 + unhalfchild, 2 + min(child)
        1 -> 3 + unhalfChild, 6 + min(child) 
        2 -> 10 + unhalfchild, 20 + min(child)
        3 -> 6 + unhalfchild, 12 + min(child)
        """
        @cache
        def dfs(parent, node, isHalfed):
            
            full_p, half_p = 0, 0
            for child in graph[node]:
                if child != parent:
                    curr_f, curr_h = dfs(node, child, True)
                    full_p += curr_f
                    half_p += min(curr_f, curr_h)
            
            return half_p + (count[node] * price[node]), full_p + (count[node] * (price[node]//2))
          
        total = min(dfs(-1, 0, False))
            
        return total
        
            