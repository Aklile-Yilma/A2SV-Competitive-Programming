class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        # stop: bus_idx
        graph = {}
        
        for idx in range(len(routes)):
            for route in routes[idx]:
                graph[route] = graph.get(route, []) + [idx]
                            
        q = deque()
        q.append((source, 0))
        visited = {source}
        visited_routes = set()
        
        while q:
            node, step = q.popleft()
            if node == target:
                return step
            
            for bus_idx in graph[node]:
                if bus_idx in visited_routes:
                    continue
                    
                for route in routes[bus_idx]:
                    if route not in visited:
                        q.append((route, step+1))
                        visited.add(route)
                        visited_routes.add(bus_idx)
            
        return -1
            