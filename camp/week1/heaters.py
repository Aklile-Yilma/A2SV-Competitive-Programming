class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        houses.sort()
        heaters.sort()
        n = len(heaters)
        max_rad = float('-inf')
        
        for house in houses:
            low = 0
            high = len(heaters)-1
            min_rad = float('inf')
            
            while low <= high:
                mid = (low + high) // 2
                min_rad = min(min_rad, abs(house-heaters[mid]))
                
                if heaters[mid] < house:
                    low = mid + 1
                else:
                    high = mid - 1
                    
            max_rad = max(max_rad, min_rad)
        
        
        return max_rad