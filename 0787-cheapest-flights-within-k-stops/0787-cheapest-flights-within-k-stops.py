class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = defaultdict(list)
        for start, stop, price in flights:
            graph[start].append((stop, price))
        
        visited = set()
        heap = []
        # weight, node, k
        heappush(heap, [0, src, k+1])
      
        while heap:
            curr_weight, node, stops = heappop(heap)

            if node == dst:
                return curr_weight
            
            if (node, stops) in visited:
                continue
            
            visited.add((node, stops))

            for neighbor, price in graph[node]:
                if stops > 0:
                    heappush(heap, [curr_weight + price, neighbor, stops-1])
                    
        return -1