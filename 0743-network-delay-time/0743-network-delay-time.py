class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        
        graph = defaultdict(list)
        
        for src, dst, weight in times:
            graph[src].append((dst, weight))
            
        distance = [float('inf')] * n
        heap = []
        # weight, src
        heappush(heap, (0, k))
        visited = set()
        
        while heap:
            curr_weight, node = heappop(heap)
            distance[node-1] = min(distance[node-1], curr_weight)
            if node in visited:
                continue
                
            visited.add(node)
            for child in graph[node]:
                dst, weight = child
                curr_distance = curr_weight + weight
                if curr_distance < distance[dst-1]:
                    heappush(heap, (curr_distance, dst))
        
        max_dist = 0
        
        for dis in distance:
            max_dist = max(max_dist, dis)
            
        return max_dist if max_dist != float('inf') else -1