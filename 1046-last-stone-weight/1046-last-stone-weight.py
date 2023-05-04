class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        for idx in range(len(stones)):
            stones[idx] = -stones[idx]
            
        #becomes a heap array
        heapify(stones)
        
        while stones:
            first = heappop(stones)
            if not stones:
                return -first
            second = heappop(stones)
            if first != second:
                heappush(stones, -abs(first-second))
                
        return 0
            
            
            
        