class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        
        graph = defaultdict(list)
        
        for idx in range(len(edges)):
            src, dst = edges[idx]
            weight = succProb[idx]
            graph[src].append((dst, weight))
            graph[dst].append((src, weight))
            
        distance = [float('-inf')] * n
        heap = []
        # weight, src
        heappush(heap, (0, start_node))
        visited = set()
        
        while heap:
            curr_weight, node = heappop(heap)
            curr_weight  = 1-curr_weight
            distance[node] = max(distance[node], curr_weight)
            
            if (node, curr_weight) in visited:
                continue
                
            visited.add((node, curr_weight))
            for child in graph[node]:
                dst, weight = child
                curr_distance = curr_weight * weight
                if curr_distance > distance[dst]:
                    heappush(heap, (1-curr_distance, dst))


        return distance[end_node] if distance[end_node] != float('-inf') else 0.0        