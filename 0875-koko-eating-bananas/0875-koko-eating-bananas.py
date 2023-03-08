class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def checkPiles(piles, h, mid):
            
            curr_hour = 0
            
            for pile in piles:
                if pile <= mid:
                    curr_hour += 1
                else:
                    curr_hour += math.ceil(pile/mid)
                    
            if curr_hour <= h:
                return True
            
            return False
        
        
        low = 1
        high = max(piles)
        
        while low <= high:
            mid = (low + high) // 2
            
            if checkPiles(piles, h, mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low
                
                
        