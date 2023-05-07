class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        heap = []
        #create a max heap
        for pile in piles:
            heappush(heap, -pile)
            
        for _ in range(k):
            stones = abs(heappop(heap))
            stones -= stones // 2
            heappush(heap, -stones)
        
        return -sum(heap)
            
        