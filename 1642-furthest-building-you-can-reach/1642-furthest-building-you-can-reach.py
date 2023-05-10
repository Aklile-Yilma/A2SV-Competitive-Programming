class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        max_heap = []
        prev = 0
        for curr in range(1, len(heights)):
            curr_gap = heights[curr] - heights[prev]
            if curr_gap <= 0:
                prev += 1
                continue
            
            heappush(max_heap, -curr_gap)
            
            if bricks - curr_gap < 0:
                if not ladders:
                    break
                max_gap = -heappop(max_heap)
                bricks += max_gap
                ladders -= 1
        
            bricks -= curr_gap
            prev += 1
            
        return prev