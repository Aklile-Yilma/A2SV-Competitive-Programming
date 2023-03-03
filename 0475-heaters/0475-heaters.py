class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        
        heaters.sort()
        houses.sort()
        
        max_radius = 0
                
        for house in houses:
            
            low = 0
            high = len(heaters)-1
            min_radius = float('inf')
            
            while low <= high:
                mid = (low + high) // 2
                
                if heaters[mid] < house:
                    min_radius = min(min_radius, abs(house-heaters[mid]))
                    low = mid + 1                                        
                elif heaters[mid] > house:
                    min_radius = min(min_radius, abs(house-heaters[mid]))
                    high = mid - 1
                else:
                    min_radius = 0
                    break
                    
            max_radius = max(min_radius, max_radius)
            
        return max_radius