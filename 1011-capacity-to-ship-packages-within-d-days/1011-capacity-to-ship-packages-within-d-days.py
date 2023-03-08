class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        def checkCapacity(weights, days, mid):
            curr_day = 1
            curr_weight = 0
            
            for weight in weights:
                if mid - curr_weight >= weight:
                    curr_weight += weight
                else:
                    curr_day += 1
                    curr_weight = weight
                    
            if curr_day <= days:
                return True
            
            return False
        
        low = max(weights)
        high = sum(weights)
        
        while low <= high:
            mid = (low + high) // 2
            if checkCapacity(weights, days, mid):
                high = mid - 1
            else:
                low = mid + 1
                
        return low
                
                
        
        
            
        
        
        
        